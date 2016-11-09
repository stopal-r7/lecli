import requests


def _url():
    """
    Get rest query url of a specific path.
    """
    return 'https://rest.logentries.com/scheduled_queries/'


def response_error(response):
    """
    Check response if it has any errors.
    """
    if response.headers.get('X-RateLimit-Remaining') is not None:
        if int(response.headers['X-RateLimit-Remaining']) == 0:
            print 'Error: Rate Limit Reached, will reset in ' + response.headers.get(
                'X-RateLimit-Reset') + ' seconds'
            return True

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print "Request Error:", error.message
        return True

    if response.status_code == 200:
        if response.headers['Content-Type'] != 'application/json':
            print 'Unexpected Content Type Received in Response: ' + response.headers[
                'Content-Type']
            return True
        else:
            return False

    return False


def get_scheduled_query(scheduled_query_id):
    pass


def list_scheduled_queries():
    pass


def create_scheduled_query(name, query):
    pass


def delete_schuled_query(scheduled_query_id):
    pass


def rename_scheduled_query(scheduled_query_id, name):
    pass


def update_query_scheduled_query(scheduled_query_id, query):
    pass
