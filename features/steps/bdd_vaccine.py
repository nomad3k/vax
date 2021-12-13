from behave import given, when, then
from datetime import date
from vaccine import Vaccine


@given(u"vaccine {name}")
def step_vaccine(context, name):
    context.vaccines[name] = Vaccine(name, name)
    pass


@given(u"{name} has {doses:Number} doses with {interval:Number} day interval")
def step_configure_vaccine(context, name: str, doses: int, interval: int):
    v = context.vaccines[name]
    v.configure(doses, interval)
    pass


@when(u"I check {a:Date} to {b:Date} satisfies the {vaccine_name} interval")
def step_satisfies_vaccine(context, a: date, b: date, vaccine_name: str):
    v = context.vaccines[vaccine_name]
    context.actual = v.satisfies_interval(a, b)
    pass


@then(u"the answer is {expected:Bool}")
def step_expect_bool(context, expected: bool):
    assert context.actual == expected, f"Expected {expected} got {context.actual}"
