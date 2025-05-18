from tinydb import TinyDB, Query

# Initialize DB
db = TinyDB('db.json')
Phone = Query()

# ✅ 1. Add or update entry by phoneId
def upsert_entry(phone_id, name, thread_id):
    # Check if entry exists
    if db.contains(Phone.phoneId == phone_id):
        db.update({'name': name, 'threadId': thread_id}, Phone.phoneId == phone_id)
    else:
        db.insert({'phoneId': phone_id, 'name': name, 'threadId': thread_id})

# ✅ 2. Get entry by phoneId
def get_entry(phone_id):
    result = db.search(Phone.phoneId == phone_id)
    return result if result else None

# ✅ 3. Delete entry by phoneId (if needed)
def delete_entry(phone_id=None, delete_all=False):
    if delete_all:
        db.truncate()  # Clears all entries in the database
    elif phone_id is not None:
        db.remove(Phone.phoneId == phone_id)

if __name__ == "__main__":
    # Example usage
    delete_entry('917982850447')
