from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matchers=None):
        self._matchers = matchers or []

    def plays_in(self, team):
        return QueryBuilder(self._matchers + [PlaysIn(team)])

    def has_at_least(self, value, attr):
        return QueryBuilder(self._matchers + [HasAtLeast(value, attr)])

    def has_fewer_than(self, value, attr):
        return QueryBuilder(self._matchers + [HasFewerThan(value, attr)])

    def one_of(self, *builders):
        built_matchers = [b.build() for b in builders]
        return QueryBuilder([Or(*built_matchers)])

    def build(self):
        if not self._matchers:
            return All()
        if len(self._matchers) == 1:
            return self._matchers[0]
        return And(*self._matchers)
