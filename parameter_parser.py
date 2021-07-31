import lark
from lark import Tree
from lark.lexer import Token

parser = lark.Lark(
    r"""
    FUNC_NAME: /[#]\w+:/
    TEMPLATE_NAME: /[^{}=|#]+/
    ARG_NAME: /[^{}=#|]+/
    TEXT: /[^{}=|]+/
    NOINCLUDE: /<noinclude>.+?<.noinclude>|<!--.+?-->/

    text: (func | template | param | TEXT)*                         -> text
    func: "{{" FUNC_NAME fung_args "}}"                             -> func
    fung_args: fun_arg ("|" fun_arg)*                               -> fung_args
    fun_arg: text | (ARG_NAME "=" text)
    template: "{{" TEMPLATE_NAME template_args "}}"                 -> template
    template_args: ("|" tpl_arg)*                                   -> template_args
    tpl_arg: (ARG_NAME "=")? text                                   -> tpl_arg
    param: "{{{" ARG_NAME ("|" text | "|")? "}}}"                   -> param

    %import common.WS
    %ignore WS
    %ignore NOINCLUDE
    """,
    start='text',
    parser='earley'
)


class TemplateCall(object):
    def __init__(self, name, args):
        self.name = name
        self.args = args


class Interpretation(object):
    def __init__(self, context):
        self.ctx = context

    def __call__(self, arg):
        print("C", arg)
        if isinstance(arg, Tree):
            print("argdat", arg.data)
            return getattr(self, arg.data, self._unknown)(arg)
        elif isinstance(arg, Token):
            return getattr(self, arg.type)(arg)

    def TEXT(self, node):
        return node.value

    def FUNC_NAME(self, node):
        return node.value

    def TEMPLATE_NAME(self, node):
        return node.value

    def ARG_NAME(self, node):
        return node.value

    def text(self, node):
        print("text", node)
        for child in node.children:
            self(child)

    def _unknown(self, node):
        print("UNKNOWN", node.data, node)

    def param(self, node):
        print("param", node)

    def fung_args(self, node):
        print([self(c) for c in node.children])

    def tpl_arg(self, node):
        print([self(c) for c in node.children])

    def template_args(self, node):
        return [self(c) for c in node.children]

    def template(self, node):
        name = node.children[0].value
        tpl = TemplateCall(name, [self(c) for c in node.children[1:]])
        print(tpl)
        return tpl

    def func(self, node):
        print("F", node)


if __name__ == "__main__":
    ex2 = """{{ТЕМП <noinclude>.dddd</noinclude>|знач1|пар2=знач2|знач3|{{{4}}}}} """

    parsed = parser.parse(ex2)
    I = Interpretation({})
    print((I(parsed)))

    example = """{{#if:{{{безличный|}}}||{{{основа}}}ал<br >{{{основа}}}ала<br />}}{{{основа}}}ало"""
    #example = """{{по-слогам|гро|мо|зди́ть}}"""
    # example = """{{#if:|aaa}}{{{основа}}}ало"""
    parsed = parser.parse(example)
    I = Interpretation({})
    print((I(parsed)))

    ex2 = """{{гл ru 4b-т  |основа=громозд |основа1=громозж |слоги={{по-слогам|гро|мо|зди́ть}} |соотв=нагромоздить |ПричСтрадНет=1}}"""

    parsed = parser.parse(ex2)
    I = Interpretation({})
    print((I(parsed)))
