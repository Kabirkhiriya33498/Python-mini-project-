from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class AuctionItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    starting_bid = db.Column(db.Float, nullable=False)
    current_bid = db.Column(db.Float, nullable=True)
    end_time = db.Column(db.DateTime, nullable=False)

with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def index():
    items = AuctionItem.query.all()
    return render_template('index.html', items=items)

# Create new auction
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        starting_bid = float(request.form['starting_bid'])
        end_time = datetime.strptime(request.form['end_time'], '%Y-%m-%d %H:%M:%S')
        new_item = AuctionItem(title=title, description=description, starting_bid=starting_bid, current_bid=starting_bid, end_time=end_time)
        db.session.add(new_item)
        db.session.commit()
        flash('Auction created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html')

# Auction details and bid
@app.route('/auction/<int:item_id>', methods=['GET', 'POST'])
def auction(item_id):
    item = AuctionItem.query.get_or_404(item_id)
    if request.method == 'POST':
        bid = float(request.form['bid'])
        if bid > item.current_bid:
            item.current_bid = bid
            db.session.commit()
            flash('Bid placed successfully!', 'success')
        else:
            flash('Bid must be higher than the current bid.', 'danger')
    return render_template('auction.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)

    
