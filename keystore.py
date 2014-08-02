import os
import ast
class KeyStore:
    def __init__(self, name, memory=False):
        self.db = {}
        self.memory = memory
        if not self.memory:
            if not os.path.exists('./keystores/'):
                os.mkdir('./keystores/')
            if os.path.exists('./keystores/%s.ks' % name):
                with open('./keystores/%s.ks' % name, 'r') as f:
                    for line in f.readlines():
                        if not line.startswith('//'): # if comment
                            key, value = line.split(' => ')
                            self.db[key] = value.strip()
                        else:
                            pass #self.db['`COMMENTS'].append(line.strip())

            self.path = './keystores/%s.ks' % name

    def _save(self):
        ''' Write all changes the the KeyStore file '''
        if not self.memory:
            with open(self.path, 'w') as f:
                for key in self.db:
                    f.write('%s => %s\n' % (key, self.db[key]))
    
    def _reload(self):
        ''' Reload the KeyStore File '''
        self.db = {}
        with open(self.path, 'r') as f:
            for line in f.readlines():
                key, value = line.split(' => ')
                self.db[key] = value.strip()
    
    def get_all(self):
        '''Returns all the key, value pairs'''
        for key in self.db:
            yield (key, self.db[key])

    def get(self, key):
        '''Get the value of a key'''
        return self.db.get(key)

    def set(self, key, value, autosave=True):
        '''Set the value of a key'''
        self.db[key] = value
        if autosave: self._save()

    def delete(self, key, autosave=True):
        '''Remove a key'''
        del self.db[key]
        if autosave: self._save()

    def convert(self, key):
        '''Evaluate an expression node or a Unicode or Latin-1 encoded string 
           containing a Python expression.'''
        return ast.literal_eval(self.get(key))
