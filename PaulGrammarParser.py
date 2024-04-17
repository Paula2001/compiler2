# Generated from PaulGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,71,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,5,2,55,8,2,10,
        2,12,2,58,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,76,8,3,1,3,1,3,3,3,80,8,3,3,3,82,8,3,3,3,84,
        8,3,1,4,1,4,1,4,1,4,3,4,90,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,110,8,7,10,7,12,7,113,
        9,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,122,8,7,10,7,12,7,125,9,7,1,
        7,3,7,128,8,7,1,8,1,8,1,8,1,8,5,8,134,8,8,10,8,12,8,137,9,8,1,8,
        1,8,3,8,141,8,8,1,9,1,9,1,9,1,9,5,9,147,8,9,10,9,12,9,150,9,9,1,
        9,1,9,1,10,1,10,1,10,1,10,5,10,158,8,10,10,10,12,10,161,9,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        5,13,190,8,13,10,13,12,13,193,9,13,1,13,1,13,5,13,197,8,13,10,13,
        12,13,200,9,13,1,13,1,13,5,13,204,8,13,10,13,12,13,207,9,13,1,13,
        1,13,5,13,211,8,13,10,13,12,13,214,9,13,1,13,1,13,5,13,218,8,13,
        10,13,12,13,221,9,13,1,13,1,13,5,13,225,8,13,10,13,12,13,228,9,13,
        1,13,1,13,5,13,232,8,13,10,13,12,13,235,9,13,1,13,1,13,5,13,239,
        8,13,10,13,12,13,242,9,13,1,13,1,13,5,13,246,8,13,10,13,12,13,249,
        9,13,1,13,1,13,5,13,253,8,13,10,13,12,13,256,9,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,264,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,280,8,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,312,8,13,10,13,12,13,315,9,13,1,13,13,111,123,135,191,
        198,205,212,219,226,233,240,247,254,1,26,14,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,0,9,1,0,58,61,3,0,10,12,27,28,42,42,1,0,29,31,1,0,
        27,28,2,0,36,37,39,40,2,0,38,38,41,41,1,0,33,35,1,0,15,26,1,0,10,
        11,370,0,29,1,0,0,0,2,50,1,0,0,0,4,52,1,0,0,0,6,83,1,0,0,0,8,89,
        1,0,0,0,10,91,1,0,0,0,12,97,1,0,0,0,14,127,1,0,0,0,16,129,1,0,0,
        0,18,142,1,0,0,0,20,153,1,0,0,0,22,164,1,0,0,0,24,171,1,0,0,0,26,
        263,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,
        0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,51,
        5,1,0,0,36,51,3,20,10,0,37,51,3,14,7,0,38,51,3,6,3,0,39,51,3,22,
        11,0,40,51,3,16,8,0,41,51,3,18,9,0,42,51,3,4,2,0,43,51,3,10,5,0,
        44,51,3,12,6,0,45,51,3,24,12,0,46,51,3,8,4,0,47,48,3,26,13,0,48,
        49,5,1,0,0,49,51,1,0,0,0,50,35,1,0,0,0,50,36,1,0,0,0,50,37,1,0,0,
        0,50,38,1,0,0,0,50,39,1,0,0,0,50,40,1,0,0,0,50,41,1,0,0,0,50,42,
        1,0,0,0,50,43,1,0,0,0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,0,0,0,
        50,47,1,0,0,0,51,3,1,0,0,0,52,56,5,2,0,0,53,55,3,2,1,0,54,53,1,0,
        0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,56,
        1,0,0,0,59,60,5,3,0,0,60,5,1,0,0,0,61,62,5,54,0,0,62,63,5,4,0,0,
        63,64,3,26,13,0,64,65,5,5,0,0,65,67,3,4,2,0,66,68,3,8,4,0,67,66,
        1,0,0,0,67,68,1,0,0,0,68,84,1,0,0,0,69,70,5,54,0,0,70,71,5,4,0,0,
        71,72,3,26,13,0,72,73,5,5,0,0,73,75,3,2,1,0,74,76,5,1,0,0,75,74,
        1,0,0,0,75,76,1,0,0,0,76,81,1,0,0,0,77,79,3,8,4,0,78,80,5,1,0,0,
        79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,77,1,0,0,0,81,82,1,
        0,0,0,82,84,1,0,0,0,83,61,1,0,0,0,83,69,1,0,0,0,84,7,1,0,0,0,85,
        86,5,55,0,0,86,90,3,4,2,0,87,88,5,55,0,0,88,90,3,2,1,0,89,85,1,0,
        0,0,89,87,1,0,0,0,90,9,1,0,0,0,91,92,5,56,0,0,92,93,5,4,0,0,93,94,
        3,26,13,0,94,95,5,5,0,0,95,96,3,4,2,0,96,11,1,0,0,0,97,98,5,57,0,
        0,98,99,3,4,2,0,99,100,5,56,0,0,100,101,5,4,0,0,101,102,3,26,13,
        0,102,103,5,5,0,0,103,104,5,1,0,0,104,13,1,0,0,0,105,106,5,67,0,
        0,106,111,5,26,0,0,107,108,5,67,0,0,108,110,5,26,0,0,109,107,1,0,
        0,0,110,113,1,0,0,0,111,112,1,0,0,0,111,109,1,0,0,0,112,114,1,0,
        0,0,113,111,1,0,0,0,114,115,3,26,13,0,115,116,5,1,0,0,116,128,1,
        0,0,0,117,118,5,67,0,0,118,123,5,26,0,0,119,120,5,67,0,0,120,122,
        5,26,0,0,121,119,1,0,0,0,122,125,1,0,0,0,123,124,1,0,0,0,123,121,
        1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,128,3,22,11,0,127,105,
        1,0,0,0,127,117,1,0,0,0,128,15,1,0,0,0,129,130,5,53,0,0,130,135,
        3,26,13,0,131,132,5,6,0,0,132,134,3,26,13,0,133,131,1,0,0,0,134,
        137,1,0,0,0,135,136,1,0,0,0,135,133,1,0,0,0,136,138,1,0,0,0,137,
        135,1,0,0,0,138,140,5,1,0,0,139,141,5,1,0,0,140,139,1,0,0,0,140,
        141,1,0,0,0,141,17,1,0,0,0,142,143,5,52,0,0,143,148,5,67,0,0,144,
        145,5,6,0,0,145,147,5,67,0,0,146,144,1,0,0,0,147,150,1,0,0,0,148,
        146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,
        152,5,1,0,0,152,19,1,0,0,0,153,154,7,0,0,0,154,159,5,67,0,0,155,
        156,5,6,0,0,156,158,5,67,0,0,157,155,1,0,0,0,158,161,1,0,0,0,159,
        157,1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,
        163,5,1,0,0,163,21,1,0,0,0,164,165,3,26,13,0,165,166,5,7,0,0,166,
        167,3,26,13,0,167,168,5,8,0,0,168,169,3,26,13,0,169,170,5,1,0,0,
        170,23,1,0,0,0,171,172,5,9,0,0,172,173,5,4,0,0,173,174,3,26,13,0,
        174,175,5,1,0,0,175,176,3,26,13,0,176,177,5,1,0,0,177,178,3,26,13,
        0,178,179,5,5,0,0,179,180,3,4,2,0,180,25,1,0,0,0,181,182,6,13,-1,
        0,182,264,5,63,0,0,183,264,5,64,0,0,184,264,5,65,0,0,185,264,5,66,
        0,0,186,264,5,67,0,0,187,191,3,16,8,0,188,190,3,2,1,0,189,188,1,
        0,0,0,190,193,1,0,0,0,191,192,1,0,0,0,191,189,1,0,0,0,192,264,1,
        0,0,0,193,191,1,0,0,0,194,198,3,20,10,0,195,197,3,2,1,0,196,195,
        1,0,0,0,197,200,1,0,0,0,198,199,1,0,0,0,198,196,1,0,0,0,199,264,
        1,0,0,0,200,198,1,0,0,0,201,205,3,14,7,0,202,204,3,2,1,0,203,202,
        1,0,0,0,204,207,1,0,0,0,205,206,1,0,0,0,205,203,1,0,0,0,206,264,
        1,0,0,0,207,205,1,0,0,0,208,212,3,18,9,0,209,211,3,2,1,0,210,209,
        1,0,0,0,211,214,1,0,0,0,212,213,1,0,0,0,212,210,1,0,0,0,213,264,
        1,0,0,0,214,212,1,0,0,0,215,219,3,6,3,0,216,218,3,2,1,0,217,216,
        1,0,0,0,218,221,1,0,0,0,219,220,1,0,0,0,219,217,1,0,0,0,220,264,
        1,0,0,0,221,219,1,0,0,0,222,226,3,8,4,0,223,225,3,2,1,0,224,223,
        1,0,0,0,225,228,1,0,0,0,226,227,1,0,0,0,226,224,1,0,0,0,227,264,
        1,0,0,0,228,226,1,0,0,0,229,233,3,10,5,0,230,232,3,2,1,0,231,230,
        1,0,0,0,232,235,1,0,0,0,233,234,1,0,0,0,233,231,1,0,0,0,234,264,
        1,0,0,0,235,233,1,0,0,0,236,240,3,12,6,0,237,239,3,2,1,0,238,237,
        1,0,0,0,239,242,1,0,0,0,240,241,1,0,0,0,240,238,1,0,0,0,241,264,
        1,0,0,0,242,240,1,0,0,0,243,247,3,24,12,0,244,246,3,2,1,0,245,244,
        1,0,0,0,246,249,1,0,0,0,247,248,1,0,0,0,247,245,1,0,0,0,248,264,
        1,0,0,0,249,247,1,0,0,0,250,254,5,1,0,0,251,253,3,2,1,0,252,251,
        1,0,0,0,253,256,1,0,0,0,254,255,1,0,0,0,254,252,1,0,0,0,255,264,
        1,0,0,0,256,254,1,0,0,0,257,258,5,4,0,0,258,259,3,26,13,0,259,260,
        5,5,0,0,260,264,1,0,0,0,261,262,7,1,0,0,262,264,3,26,13,13,263,181,
        1,0,0,0,263,183,1,0,0,0,263,184,1,0,0,0,263,185,1,0,0,0,263,186,
        1,0,0,0,263,187,1,0,0,0,263,194,1,0,0,0,263,201,1,0,0,0,263,208,
        1,0,0,0,263,215,1,0,0,0,263,222,1,0,0,0,263,229,1,0,0,0,263,236,
        1,0,0,0,263,243,1,0,0,0,263,250,1,0,0,0,263,257,1,0,0,0,263,261,
        1,0,0,0,264,313,1,0,0,0,265,266,10,12,0,0,266,267,7,2,0,0,267,312,
        3,26,13,13,268,269,10,11,0,0,269,270,7,3,0,0,270,312,3,26,13,12,
        271,279,10,10,0,0,272,273,5,37,0,0,273,280,5,37,0,0,274,275,5,36,
        0,0,275,276,5,36,0,0,276,280,5,36,0,0,277,278,5,36,0,0,278,280,5,
        36,0,0,279,272,1,0,0,0,279,274,1,0,0,0,279,277,1,0,0,0,280,281,1,
        0,0,0,281,312,3,26,13,11,282,283,10,9,0,0,283,284,7,4,0,0,284,312,
        3,26,13,10,285,286,10,8,0,0,286,287,7,5,0,0,287,312,3,26,13,9,288,
        289,10,7,0,0,289,290,5,13,0,0,290,312,3,26,13,8,291,292,10,6,0,0,
        292,293,5,33,0,0,293,312,3,26,13,7,294,295,10,5,0,0,295,296,5,14,
        0,0,296,312,3,26,13,6,297,298,10,4,0,0,298,299,7,6,0,0,299,312,3,
        26,13,5,300,301,10,3,0,0,301,302,5,32,0,0,302,312,3,26,13,4,303,
        304,10,2,0,0,304,305,5,35,0,0,305,312,3,26,13,3,306,307,10,1,0,0,
        307,308,7,7,0,0,308,312,3,26,13,1,309,310,10,14,0,0,310,312,7,8,
        0,0,311,265,1,0,0,0,311,268,1,0,0,0,311,271,1,0,0,0,311,282,1,0,
        0,0,311,285,1,0,0,0,311,288,1,0,0,0,311,291,1,0,0,0,311,294,1,0,
        0,0,311,297,1,0,0,0,311,300,1,0,0,0,311,303,1,0,0,0,311,306,1,0,
        0,0,311,309,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,
        0,0,314,27,1,0,0,0,315,313,1,0,0,0,30,31,50,56,67,75,79,81,83,89,
        111,123,127,135,140,148,159,191,198,205,212,219,226,233,240,247,
        254,263,279,311,313
    ]

class PaulGrammarParser ( Parser ):

    grammarFileName = "PaulGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'('", "')'", "','", 
                     "'?'", "':'", "'for'", "'++'", "'--'", "'~'", "'&'", 
                     "'|'", "'+='", "'-='", "'*='", "'/='", "'&='", "'|='", 
                     "'^='", "'>>='", "'>>>='", "'<<='", "'%='", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'.'", "'^'", "'&&'", 
                     "'||'", "'>'", "'<'", "'=='", "'>='", "'<='", "'!='", 
                     "'!'", "'itof'", "'push'", "'pop'", "'load'", "'save'", 
                     "'label'", "'jmp'", "'fjmp'", "'print'", "'read'", 
                     "'write'", "'if'", "'else'", "'while'", "'do'", "'int'", 
                     "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "EQ", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "APPEND", "XOR", "AND", "OR", "GT", 
                      "LT", "EQQ", "GTEQ", "LTEQ", "NOTEQ", "NOT", "ITOF", 
                      "PUSH", "POP", "LOAD", "SAVE", "LABEL", "JMP", "FJMP", 
                      "PRINT", "READ", "WRITE", "IF", "ELSE", "WHILE", "DO", 
                      "INT", "FLOAT", "BOOL", "STRING", "TYPES", "INT_LITRAL", 
                      "FLOAT_LITRAL", "BOOL_LITRAL", "STRING_LITRAL", "ID", 
                      "NEWLINE", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_ifStatement = 3
    RULE_elseStatement = 4
    RULE_whileStatement = 5
    RULE_doWhileStatement = 6
    RULE_assignment = 7
    RULE_writeStatement = 8
    RULE_readStatement = 9
    RULE_declaration = 10
    RULE_condition = 11
    RULE_forStatement = 12
    RULE_expression = 13

    ruleNames =  [ "program", "statement", "block", "ifStatement", "elseStatement", 
                   "whileStatement", "doWhileStatement", "assignment", "writeStatement", 
                   "readStatement", "declaration", "condition", "forStatement", 
                   "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    EQ=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    MOD=31
    APPEND=32
    XOR=33
    AND=34
    OR=35
    GT=36
    LT=37
    EQQ=38
    GTEQ=39
    LTEQ=40
    NOTEQ=41
    NOT=42
    ITOF=43
    PUSH=44
    POP=45
    LOAD=46
    SAVE=47
    LABEL=48
    JMP=49
    FJMP=50
    PRINT=51
    READ=52
    WRITE=53
    IF=54
    ELSE=55
    WHILE=56
    DO=57
    INT=58
    FLOAT=59
    BOOL=60
    STRING=61
    TYPES=62
    INT_LITRAL=63
    FLOAT_LITRAL=64
    BOOL_LITRAL=65
    STRING_LITRAL=66
    ID=67
    NEWLINE=68
    WS=69
    COMMENT=70
    LINE_COMMENT=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PaulGrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PaulGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -4616185219605586410) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 15) != 0)):
                    break

            self.state = 33
            self.match(PaulGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(PaulGrammarParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PaulGrammarParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.IfStatementContext,0)


        def condition(self):
            return self.getTypedRuleContext(PaulGrammarParser.ConditionContext,0)


        def writeStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.WriteStatementContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ReadStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(PaulGrammarParser.BlockContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ForStatementContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ElseStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PaulGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(PaulGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.condition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.writeStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 41
                self.readStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.block()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 43
                self.whileStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 44
                self.doWhileStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 45
                self.forStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 46
                self.elseStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 47
                self.expression(0)
                self.state = 48
                self.match(PaulGrammarParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = PaulGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PaulGrammarParser.T__1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4616185219605586410) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 15) != 0):
                self.state = 53
                self.statement()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(PaulGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PaulGrammarParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(PaulGrammarParser.BlockContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ElseStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(PaulGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = PaulGrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(PaulGrammarParser.IF)
                self.state = 62
                self.match(PaulGrammarParser.T__3)
                self.state = 63
                self.expression(0)
                self.state = 64
                self.match(PaulGrammarParser.T__4)
                self.state = 65
                self.block()
                self.state = 67
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self.elseStatement()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(PaulGrammarParser.IF)
                self.state = 70
                self.match(PaulGrammarParser.T__3)
                self.state = 71
                self.expression(0)
                self.state = 72
                self.match(PaulGrammarParser.T__4)
                self.state = 73
                self.statement()
                self.state = 75
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 74
                    self.match(PaulGrammarParser.T__0)


                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 77
                    self.elseStatement()
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 78
                        self.match(PaulGrammarParser.T__0)




                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(PaulGrammarParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(PaulGrammarParser.BlockContext,0)


        def statement(self):
            return self.getTypedRuleContext(PaulGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = PaulGrammarParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elseStatement)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(PaulGrammarParser.ELSE)
                self.state = 86
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(PaulGrammarParser.ELSE)
                self.state = 88
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PaulGrammarParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(PaulGrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = PaulGrammarParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(PaulGrammarParser.WHILE)
            self.state = 92
            self.match(PaulGrammarParser.T__3)
            self.state = 93
            self.expression(0)
            self.state = 94
            self.match(PaulGrammarParser.T__4)
            self.state = 95
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(PaulGrammarParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(PaulGrammarParser.BlockContext,0)


        def WHILE(self):
            return self.getToken(PaulGrammarParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = PaulGrammarParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(PaulGrammarParser.DO)
            self.state = 98
            self.block()
            self.state = 99
            self.match(PaulGrammarParser.WHILE)
            self.state = 100
            self.match(PaulGrammarParser.T__3)
            self.state = 101
            self.expression(0)
            self.state = 102
            self.match(PaulGrammarParser.T__4)
            self.state = 103
            self.match(PaulGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PaulGrammarParser.ID)
            else:
                return self.getToken(PaulGrammarParser.ID, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(PaulGrammarParser.EQ)
            else:
                return self.getToken(PaulGrammarParser.EQ, i)

        def expression(self):
            return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,0)


        def condition(self):
            return self.getTypedRuleContext(PaulGrammarParser.ConditionContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PaulGrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(PaulGrammarParser.ID)
                self.state = 106
                self.match(PaulGrammarParser.EQ)
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 107
                        self.match(PaulGrammarParser.ID)
                        self.state = 108
                        self.match(PaulGrammarParser.EQ) 
                    self.state = 113
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 114
                self.expression(0)
                self.state = 115
                self.match(PaulGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(PaulGrammarParser.ID)
                self.state = 118
                self.match(PaulGrammarParser.EQ)
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 119
                        self.match(PaulGrammarParser.ID)
                        self.state = 120
                        self.match(PaulGrammarParser.EQ) 
                    self.state = 125
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 126
                self.condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(PaulGrammarParser.WRITE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_writeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)




    def writeStatement(self):

        localctx = PaulGrammarParser.WriteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_writeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(PaulGrammarParser.WRITE)
            self.state = 130
            self.expression(0)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 131
                    self.match(PaulGrammarParser.T__5)
                    self.state = 132
                    self.expression(0) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 138
            self.match(PaulGrammarParser.T__0)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 139
                self.match(PaulGrammarParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(PaulGrammarParser.READ, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PaulGrammarParser.ID)
            else:
                return self.getToken(PaulGrammarParser.ID, i)

        def getRuleIndex(self):
            return PaulGrammarParser.RULE_readStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)




    def readStatement(self):

        localctx = PaulGrammarParser.ReadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(PaulGrammarParser.READ)
            self.state = 143
            self.match(PaulGrammarParser.ID)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 144
                self.match(PaulGrammarParser.T__5)
                self.state = 145
                self.match(PaulGrammarParser.ID)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(PaulGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PaulGrammarParser.ID)
            else:
                return self.getToken(PaulGrammarParser.ID, i)

        def INT(self):
            return self.getToken(PaulGrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PaulGrammarParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(PaulGrammarParser.BOOL, 0)

        def STRING(self):
            return self.getToken(PaulGrammarParser.STRING, 0)

        def getRuleIndex(self):
            return PaulGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = PaulGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4323455642275676160) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 154
            self.match(PaulGrammarParser.ID)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 155
                self.match(PaulGrammarParser.T__5)
                self.state = 156
                self.match(PaulGrammarParser.ID)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(PaulGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = PaulGrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.expression(0)
            self.state = 165
            self.match(PaulGrammarParser.T__6)
            self.state = 166
            self.expression(0)
            self.state = 167
            self.match(PaulGrammarParser.T__7)
            self.state = 168
            self.expression(0)
            self.state = 169
            self.match(PaulGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,i)


        def block(self):
            return self.getTypedRuleContext(PaulGrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return PaulGrammarParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = PaulGrammarParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PaulGrammarParser.T__8)
            self.state = 172
            self.match(PaulGrammarParser.T__3)
            self.state = 173
            self.expression(0)
            self.state = 174
            self.match(PaulGrammarParser.T__0)
            self.state = 175
            self.expression(0)
            self.state = 176
            self.match(PaulGrammarParser.T__0)
            self.state = 177
            self.expression(0)
            self.state = 178
            self.match(PaulGrammarParser.T__4)
            self.state = 179
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # Token
            self.bop = None # Token
            self.postfix = None # Token

        def INT_LITRAL(self):
            return self.getToken(PaulGrammarParser.INT_LITRAL, 0)

        def FLOAT_LITRAL(self):
            return self.getToken(PaulGrammarParser.FLOAT_LITRAL, 0)

        def BOOL_LITRAL(self):
            return self.getToken(PaulGrammarParser.BOOL_LITRAL, 0)

        def STRING_LITRAL(self):
            return self.getToken(PaulGrammarParser.STRING_LITRAL, 0)

        def ID(self):
            return self.getToken(PaulGrammarParser.ID, 0)

        def writeStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.WriteStatementContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.StatementContext,i)


        def declaration(self):
            return self.getTypedRuleContext(PaulGrammarParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PaulGrammarParser.AssignmentContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ReadStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.IfStatementContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ElseStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(PaulGrammarParser.ForStatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PaulGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PaulGrammarParser.ExpressionContext,i)


        def ADD(self):
            return self.getToken(PaulGrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(PaulGrammarParser.SUB, 0)

        def NOT(self):
            return self.getToken(PaulGrammarParser.NOT, 0)

        def MUL(self):
            return self.getToken(PaulGrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(PaulGrammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(PaulGrammarParser.MOD, 0)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(PaulGrammarParser.LT)
            else:
                return self.getToken(PaulGrammarParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(PaulGrammarParser.GT)
            else:
                return self.getToken(PaulGrammarParser.GT, i)

        def LTEQ(self):
            return self.getToken(PaulGrammarParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(PaulGrammarParser.GTEQ, 0)

        def EQQ(self):
            return self.getToken(PaulGrammarParser.EQQ, 0)

        def NOTEQ(self):
            return self.getToken(PaulGrammarParser.NOTEQ, 0)

        def XOR(self):
            return self.getToken(PaulGrammarParser.XOR, 0)

        def AND(self):
            return self.getToken(PaulGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(PaulGrammarParser.OR, 0)

        def APPEND(self):
            return self.getToken(PaulGrammarParser.APPEND, 0)

        def EQ(self):
            return self.getToken(PaulGrammarParser.EQ, 0)

        def getRuleIndex(self):
            return PaulGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PaulGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 182
                self.match(PaulGrammarParser.INT_LITRAL)
                pass

            elif la_ == 2:
                self.state = 183
                self.match(PaulGrammarParser.FLOAT_LITRAL)
                pass

            elif la_ == 3:
                self.state = 184
                self.match(PaulGrammarParser.BOOL_LITRAL)
                pass

            elif la_ == 4:
                self.state = 185
                self.match(PaulGrammarParser.STRING_LITRAL)
                pass

            elif la_ == 5:
                self.state = 186
                self.match(PaulGrammarParser.ID)
                pass

            elif la_ == 6:
                self.state = 187
                self.writeStatement()
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 188
                        self.statement() 
                    self.state = 193
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 7:
                self.state = 194
                self.declaration()
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 195
                        self.statement() 
                    self.state = 200
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 8:
                self.state = 201
                self.assignment()
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 202
                        self.statement() 
                    self.state = 207
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass

            elif la_ == 9:
                self.state = 208
                self.readStatement()
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 209
                        self.statement() 
                    self.state = 214
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass

            elif la_ == 10:
                self.state = 215
                self.ifStatement()
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 216
                        self.statement() 
                    self.state = 221
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass

            elif la_ == 11:
                self.state = 222
                self.elseStatement()
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 223
                        self.statement() 
                    self.state = 228
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass

            elif la_ == 12:
                self.state = 229
                self.whileStatement()
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 230
                        self.statement() 
                    self.state = 235
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 13:
                self.state = 236
                self.doWhileStatement()
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 237
                        self.statement() 
                    self.state = 242
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                pass

            elif la_ == 14:
                self.state = 243
                self.forStatement()
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 244
                        self.statement() 
                    self.state = 249
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass

            elif la_ == 15:
                self.state = 250
                self.match(PaulGrammarParser.T__0)
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 251
                        self.statement() 
                    self.state = 256
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 16:
                self.state = 257
                self.match(PaulGrammarParser.T__3)
                self.state = 258
                self.expression(0)
                self.state = 259
                self.match(PaulGrammarParser.T__4)
                pass

            elif la_ == 17:
                self.state = 261
                localctx.prefix = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4398449171456) != 0)):
                    localctx.prefix = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.expression(13)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 311
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 265
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 266
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 267
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 268
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 269
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 270
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 271
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 279
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                        if la_ == 1:
                            self.state = 272
                            self.match(PaulGrammarParser.LT)
                            self.state = 273
                            self.match(PaulGrammarParser.LT)
                            pass

                        elif la_ == 2:
                            self.state = 274
                            self.match(PaulGrammarParser.GT)
                            self.state = 275
                            self.match(PaulGrammarParser.GT)
                            self.state = 276
                            self.match(PaulGrammarParser.GT)
                            pass

                        elif la_ == 3:
                            self.state = 277
                            self.match(PaulGrammarParser.GT)
                            self.state = 278
                            self.match(PaulGrammarParser.GT)
                            pass


                        self.state = 281
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 282
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 283
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1855425871872) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 284
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 285
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 286
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==38 or _la==41):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 287
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 288
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 289
                        localctx.bop = self.match(PaulGrammarParser.T__12)
                        self.state = 290
                        self.expression(8)
                        pass

                    elif la_ == 7:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 291
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 292
                        localctx.bop = self.match(PaulGrammarParser.XOR)
                        self.state = 293
                        self.expression(7)
                        pass

                    elif la_ == 8:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 294
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 295
                        localctx.bop = self.match(PaulGrammarParser.T__13)
                        self.state = 296
                        self.expression(6)
                        pass

                    elif la_ == 9:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 297
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 298
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 299
                        self.expression(5)
                        pass

                    elif la_ == 10:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 300
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 301
                        localctx.bop = self.match(PaulGrammarParser.APPEND)
                        self.state = 302
                        self.expression(4)
                        pass

                    elif la_ == 11:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 303
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 304
                        localctx.bop = self.match(PaulGrammarParser.OR)
                        self.state = 305
                        self.expression(3)
                        pass

                    elif la_ == 12:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 306
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 307
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134184960) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 308
                        self.expression(1)
                        pass

                    elif la_ == 13:
                        localctx = PaulGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 309
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 310
                        localctx.postfix = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.postfix = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 14)
         




