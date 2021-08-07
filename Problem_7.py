# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('/')
        self.root.handle = root_handler

    def insert(self, S_URL, handler):   
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # Add a word to the Trie.
        if S_URL is None or len(S_URL) == 0:
            return

        # start from root.
        curr = self.root
        for part in S_URL:
            # if char not child to curr node add it as child.
            if part not in curr.children:
                curr.insert(part)
            # go deep for one step.
            curr = curr.children[part]

        curr.handle = handler

    def find(self, S_URL):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if S_URL is None:
            return
        # start from root
        curr = self.root
        for part in S_URL:
            if part in curr.children:
                curr = curr.children.get(part)
            else:
                return None

        return curr.handle


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, part):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handle = None
        self.part = part

    def insert(self, part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode(part)


# The Router class will wrap the Trie and handle
def split_path(path):
    # you need to split the path into parts for
    # both the add_handler and loop up functions,
    # so it should be placed in a function here
    temp = path.split('/')
    return [i for i in temp if i != '']


class Router:
    def __init__(self, root_handle):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handle)

    def add_handler(self, path , handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        s_path = split_path(path)
        self.router.insert(s_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        S_path = split_path(path)
        return self.router.find(S_path)


# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
