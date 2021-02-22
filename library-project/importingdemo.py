from importingdemo.libraryabc import feedme as fm, Foobar as Foo, Calendar as Cal, Bor, Monday
from importingdemo.accounting import Accounting as Acct, Monday as Mon
from limeutils import split_fullname


foo_obj = Foo()
foo_obj.message('Hello world')
fm()

cal = Cal()
borobj = Bor()

acct = Acct()



if __name__ == '__main__':
    pass