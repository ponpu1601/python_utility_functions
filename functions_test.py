import unittest
import functions

class FunctionsTester(unittest.TestCase):

    def test_list_each_digit(self):

        # オプションなしで先頭から一桁ずつリスト化されること
        value = 123456
        expect = [1,2,3,4,5,6]
        self.assertEqual(functions.list_each_digit(value),expect)

        # オプションを明示的に指定して先頭から一桁ずつリスト化されること
        self.assertEqual(functions.list_each_digit(value,False),expect)

        # オプションTrueで末尾から一桁ずつリスト化されること
        expect = [6,5,4,3,2,1]
        self.assertEqual(functions.list_each_digit(value,True),expect)

        # 対象数値が一桁の場合でも一つの要素を持つリストとなること
        value = 1
        expect = [1]
        self.assertEqual(functions.list_each_digit(value),expect)

        # 0のみの数字列の場合は0が一つだけ含まれたリストとなること
        value = 00000
        expect = [0]
        self.assertEqual(functions.list_each_digit(value),expect)

        # マイナス値の場合でも符号を除いて一桁ずつリスト化されること
        value = -123456
        expect = [1,2,3,4,5,6]
        self.assertEqual(functions.list_each_digit(value),expect)

        # 文字列での呼び出しはTypeErrorが発生する
        value = '123456'
        with self.assertRaises(TypeError):
            functions.list_each_digit(value)
        
        # Noneを渡すとTypeErrorが発生する
        value = None
        with self.assertRaises(TypeError):
            functions.list_each_digit(value)
    
    def test_index_lists(self):
        #dictのリストの場合
        value = [{'id':1,'name':'aaa'},{'id':2,'name':'bbb'},{'id':3,'name':'ccc'}]
        
        ## keyとする値にidを指定
        expect = {1:{'id':1,'name':'aaa'},2:{'id':2,'name':'bbb'},3:{'id':3,'name':'ccc'}}
        self.assertEqual(functions.index_lists(value,'id'),expect)
        ## keyとする値にnameを指定
        expect = {'aaa':{'id':1,'name':'aaa'},'bbb':{'id':2,'name':'bbb'},'ccc':{'id':3,'name':'ccc'}}
        self.assertEqual(functions.index_lists(value,'name'),expect)

        #listのリストの場合
        value = [[1,2,3],[4,5,6],[7,8,9]]
        
        ## keyとする値に2番目の値を指定
        expect = {2:[1,2,3],5:[4,5,6],8:[7,8,9]}
        self.assertEqual(functions.index_lists(value,1),expect)

        ## keyに指定した値に重複があった場合は例外が発生する
        value=[[1,2,3],[4,5,6],[7,8,9],[2,2,2]]
        with self.assertRaises(Exception):
            functions.index_lists(value,1)

        # keyに変更可能オブジェクトを指定した場合はTypeErrorが発生する
        ## listを指定
        value = [{'id':1,'friends':[2,3,4]},{'id':2,'friends':[1,3,4]},{'id':3,'friends':[1,2,4]},{'id':4,'friends':[1,2,3]}]
        with self.assertRaises(TypeError):
            functions.index_lists(value,'friends')
        
        ## dictを指定
        value = [{'id':1,'friends':{2:'bbb',3:'ccc',4:'ddd'}},{'id':2,'friends':{1:'aaa',3:'ccc',4:'ddd'}},{'id':3,'friends':{1:'aaa',2:'bbb',4:'ddd'}},{'id':4,'friends':{2:'bbb',3:'ccc',1:'aaa'}}]
        with self.assertRaises(TypeError):
            functions.index_lists(value,'friends')
        






