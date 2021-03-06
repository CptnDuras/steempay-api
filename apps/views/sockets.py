from flask import Flask, Blueprint, jsonify
from flask_socketio import send, emit

from helpers import get_account_history, get_steem_account

steem_socket = Blueprint(r'ws', __name__)


@steem_socket.route("/<username>")
def get_user(username):
    account = get_steem_account(username)

    return jsonify(account)


@steem_socket.route("/<username>/history/<limit>")
def get_transaction_history(username, limit, socket):
    history = get_account_history(username, limit)

    return jsonify(history)


@steem_socket.route("/<username>/history")
def get_transaction_history_all(username):
    history = get_account_history(username)

    return jsonify(history)


@steem_socket.route("/<username>/attribute/<attribute>")
def get_user_attribute(username, attribute):
    account = get_steem_account(username)

    if attribute in account.keys():
        return jsonify(account[attribute])
    else:
        return jsonify({})