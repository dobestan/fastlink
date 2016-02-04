from hashids import Hashids


def _get_hashid_object(instance):
    return Hashids(salt=instance.__class__.__name__, min_length=4)


def get_encoded_hashid(instance):
    hashid = _get_hashid_object(instance)
    return hashid.encode(instance.id)
