# from data_structures.hashtable import Hashtable

def left_join(left_hash, right_hash):
    hashtable_combine = []

    for key in left_hash:
        hashtable_combine.append(key)
        hashtable_combine.append(left_hash[key])

        if key in right_hash:
            hashtable_combine.append(right_hash[key])
        else:
            hashtable_combine.append(None)

    return hashtable_combine
