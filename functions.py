
def list_each_digit(num:int,reverse=False)->list:
    """
    渡された数値を一桁ずつのint配列にして返す
    デフォルトで先頭から
    reverse=Trueで末尾から
    """
    each_digit = [int(i) for i in list(str(abs(num)))]
    if reverse:
        each_digit.reverse()
    return each_digit
    
def is_odd(num:int)->bool:

    return num & 1


def index_lists(target_lists,key_index)->dict:
    """
    リスト(dict含む)のリストから指定された要素の値をkeyとした辞書型オブジェクトを作成
    指定した要素に重複がある場合は例外を返す
    """
    keys = [item[key_index] for item in target_lists]
    if len(keys) != len(set(keys)):
        raise Exception('there is some overlap between elements specified as key')    
    return dict(map(lambda item:(item[key_index],item),target_lists))
