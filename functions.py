import requests
import pytest

def get_posts(ENDPOINT):
    return requests.get(ENDPOINT)

def create_post(payload, ENDPOINT):
    return requests.post(ENDPOINT, data=payload)

def new_post_payload():
    return {
        "userId": 13,
        "title": "i love metallica",
        "body": "metallica is the best band in the world"
    }

def wrong_payload():
    return {
        'id': 345
    }

def get_post_by_id(post_id, ENDPOINT):
    return requests.get(ENDPOINT + f"/{post_id}")

def delete_post(post_id, ENDPOINT):
    return requests.delete(ENDPOINT + f"/{post_id}")