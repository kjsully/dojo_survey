
from ..config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.location = data['location'],
        self.language = data['language'],
        self.comment = data['comment'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],




    @staticmethod
    def validate_user(post_data):
        is_valid = True

        if len(post_data['name']) < 1:
            flash('*All Fields Required')
            is_valid = False

        if len(post_data['location']) < 1:
            flash('*All Fields Required')
            is_valid = False

        if len(post_data['language']) < 1:
            flash('*All Fields Required')
            is_valid = False

        return is_valid
