import ipdb

class Author:

    all = []

    def __init__(self, name):
        self.name = name

        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        Contract.all.append(new_contract)
        return new_contract

    def total_royalties(self):
        royalties_list = [contract.royalties for contract in self.contracts()]
        return sum(royalties_list)
        
    


class Book:

    all = []

    def __init__(self, title):
        self.title = title

        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]
    


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author_param):
        if(isinstance(author_param, Author)):
            self._author = author_param
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book_param):
        if(isinstance(book_param, Book)):
            self._book = book_param
        else:
            raise Exception
        
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date_param):
        if(isinstance(date_param, str)):
            self._date = date_param
        else:
            raise Exception
        
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties_param):
        if(isinstance(royalties_param, int)):
            self._royalties = royalties_param
        else:
            raise Exception


    @classmethod
    def contracts_by_date(cls, date):
        sorted_contracts = sorted(cls.all, key= lambda d: d.date)
        new_contracts = [contract for contract in sorted_contracts if contract.date == date]
        return new_contracts
        
        


# ipdb.set_trace()
