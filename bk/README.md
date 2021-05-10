<h1>Book Inventory system</h1>
As the name suggest, it helps the user to maintain it's book store. It helps to keep
track of inventory (i.e.,number of copies) you have on every book.

**Features**

* It lists all stores for the user.
* It lists out all the books in inventory.
* Make changes to inventory:
  * Add a new book. 
  * Update inventory for an existing book. 
  * Remove from the inventory.
    
**Installation**
```angular2html
# clone this repo with git
$ git clone https://github.com/aryanjain1/book_inventory.git

$ python -m venv environment_name

$ source environment_name/bin/activate

$ pip install -r requirements.txt

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver


```
