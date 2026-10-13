from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(200))
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.text}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = Todo(text=request.form['todo'], note=request.form['note'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)
    p = db.paginate(todo_query().statement, page=page, per_page=5,
                    error_out=False)
    return render_template('index.html', todos=p.items, p=p)

def todo_query():
    query = Todo.query
    status = request.args.get('status', 'all')
    if status == 'done':
        query = query.filter_by(done=True)
    elif status == 'pending':
        query = query.filter_by(done=False)

    sort = request.args.get('sort', 'oldest')
    if sort == 'newest':
        return query.order_by(Todo.id.desc())
    if sort == 'text':
        return query.order_by(Todo.text)
    return query.order_by(Todo.id)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    todos = todo_query().filter(Todo.text.like(f'%{q}%')).all()
    return render_template('index.html', todos=todos)

@app.route('/toggle/<int:id>')
def toggle(id):
    todo = db.get_or_404(Todo, id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    todo = db.get_or_404(Todo, id)
    todo.text = request.form['todo']
    todo.note = request.form['note']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = db.get_or_404(Todo, id)
    if request.method == 'POST':
        todo.text = request.form['todo']
        todo.note = request.form['note']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = db.get_or_404(Todo, id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
