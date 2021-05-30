def login(id, pw):
    if(id == 'yelim' and pw == 'yelime'):
        return True
    else:
        return False
print("login('admin','1234'):", login('admin','1234'))
print("login(pw='yelime',id='yelim') :", login(pw='yelime', id='yelim'))
print("login('yelim', 'yelime') :", login('yelim', 'yelime'))
      
