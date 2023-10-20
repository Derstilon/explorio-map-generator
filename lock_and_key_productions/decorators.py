from .utils import find_isomorphisms

def first_isomorphism(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)

        return inner
    return outer

def all_isomorphisms(left_side):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = find_isomorphisms(G, left_side)

            if not isomorphisms: return apply_fun(G, *args, **kwargs)

            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)

        return inner

    return outer

def basic_isomorphism(left_side, all_isomorphisms=False, iso_finder=find_isomorphisms):
    def outer(apply_fun):
        def inner(G, *args, **kwargs):
            isomorphisms = iso_finder(G, left_side)
            if not isomorphisms: 
                return apply_fun(G, *args, **kwargs)
            if not all_isomorphisms:
                return apply_fun(G, *args, isomorphism=isomorphisms[0], **kwargs)
            return apply_fun(G, *args, isomorphisms=isomorphisms, **kwargs)
        return inner
    return outer