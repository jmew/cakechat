class ContextManager:
    def __init__(self):
        self.contexts = []

    def _add_context(self, c):
        self.contexts.append(c)
        if len(self.contexts) > 3:
            self.contexts = self.contexts[-3:0]

    def get_contexts(self, cur_input):
        self._add_context(cur_input)
        return self.contexts

    def update_contexts(self, cur_input):
        self._add_context(cur_input)
