from tornado.routing import Rule, RuleRouter, PathMatches

from example.apps import auth

router = RuleRouter([
    Rule(PathMatches("/auth/.*"), auth.application)
])
