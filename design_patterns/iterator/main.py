from iterator.word_collection import WordCollection

if __name__ == "__main__":
    word_coll = WordCollection()
    word_coll.add_item("This")
    word_coll.add_item("is")
    word_coll.add_item("a")
    word_coll.add_item("sentence")

    for word in word_coll:
        print(word)


