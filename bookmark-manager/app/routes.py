from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Bookmark

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Homepage displaying all bookmarks"""
    search_query = request.args.get('search', '')
    tag_filter = request.args.get('tag', '')

    query = Bookmark.query

    # Apply search filter
    if search_query:
        query = query.filter(
            (Bookmark.title.contains(search_query)) |
            (Bookmark.url.contains(search_query)) |
            (Bookmark.description.contains(search_query))
        )

    # Apply tag filter
    if tag_filter:
        query = query.filter(Bookmark.tags.contains(tag_filter))

    bookmarks = query.order_by(Bookmark.created_at.desc()).all()
    all_tags = Bookmark.get_all_tags()

    return render_template('index.html',
                         bookmarks=bookmarks,
                         all_tags=all_tags,
                         search_query=search_query,
                         tag_filter=tag_filter)

@main.route('/add', methods=['GET', 'POST'])
def add_bookmark():
    """Add a new bookmark"""
    if request.method == 'POST':
        title = request.form.get('title')
        url = request.form.get('url')
        description = request.form.get('description', '')
        tags = request.form.get('tags', '')

        if not title or not url:
            flash('Title and URL are required!', 'error')
            return redirect(url_for('main.add_bookmark'))

        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        bookmark = Bookmark(
            title=title,
            url=url,
            description=description,
            tags=tags
        )

        db.session.add(bookmark)
        db.session.commit()

        flash('Bookmark added successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('add.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_bookmark(id):
    """Edit an existing bookmark"""
    bookmark = Bookmark.query.get_or_404(id)

    if request.method == 'POST':
        bookmark.title = request.form.get('title')
        bookmark.url = request.form.get('url')
        bookmark.description = request.form.get('description', '')
        bookmark.tags = request.form.get('tags', '')

        if not bookmark.title or not bookmark.url:
            flash('Title and URL are required!', 'error')
            return redirect(url_for('main.edit_bookmark', id=id))

        # Ensure URL has protocol
        if not bookmark.url.startswith(('http://', 'https://')):
            bookmark.url = 'https://' + bookmark.url

        db.session.commit()

        flash('Bookmark updated successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('edit.html', bookmark=bookmark)

@main.route('/delete/<int:id>')
def delete_bookmark(id):
    """Delete a bookmark"""
    bookmark = Bookmark.query.get_or_404(id)
    db.session.delete(bookmark)
    db.session.commit()

    flash('Bookmark deleted successfully!', 'success')
    return redirect(url_for('main.index'))
