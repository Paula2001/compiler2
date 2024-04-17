# Generated from PaulGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PaulGrammarParser import PaulGrammarParser
else:
    from PaulGrammarParser import PaulGrammarParser

# This class defines a complete listener for a parse tree produced by PaulGrammarParser.
class PaulGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by PaulGrammarParser#program.
    def enterProgram(self, ctx:PaulGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#program.
    def exitProgram(self, ctx:PaulGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#statement.
    def enterStatement(self, ctx:PaulGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#statement.
    def exitStatement(self, ctx:PaulGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#block.
    def enterBlock(self, ctx:PaulGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#block.
    def exitBlock(self, ctx:PaulGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:PaulGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:PaulGrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#elseStatement.
    def enterElseStatement(self, ctx:PaulGrammarParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#elseStatement.
    def exitElseStatement(self, ctx:PaulGrammarParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:PaulGrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:PaulGrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:PaulGrammarParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:PaulGrammarParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#assignment.
    def enterAssignment(self, ctx:PaulGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#assignment.
    def exitAssignment(self, ctx:PaulGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#writeStatement.
    def enterWriteStatement(self, ctx:PaulGrammarParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#writeStatement.
    def exitWriteStatement(self, ctx:PaulGrammarParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#readStatement.
    def enterReadStatement(self, ctx:PaulGrammarParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#readStatement.
    def exitReadStatement(self, ctx:PaulGrammarParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#declaration.
    def enterDeclaration(self, ctx:PaulGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#declaration.
    def exitDeclaration(self, ctx:PaulGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#condition.
    def enterCondition(self, ctx:PaulGrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#condition.
    def exitCondition(self, ctx:PaulGrammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#forStatement.
    def enterForStatement(self, ctx:PaulGrammarParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#forStatement.
    def exitForStatement(self, ctx:PaulGrammarParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#expression.
    def enterExpression(self, ctx:PaulGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#expression.
    def exitExpression(self, ctx:PaulGrammarParser.ExpressionContext):
        pass



del PaulGrammarParser