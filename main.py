from antlr4 import *
from PaulGrammarLexer import PaulGrammarLexer
from PaulGrammarParser import PaulGrammarParser


class DataTypeResolver:
    def __init__(self,program):
        self.dataType = None
        self.program = program
        
        

    def getOperationType(self,expression:PaulGrammarParser.ExpressionContext,leftType,rightType):
        if leftType in ['int','float'] and rightType in ['int','float']:
            if expression.ADD() or expression.SUB() or expression.MUL() or expression.DIV():
                if leftType == 'int' and rightType == 'int' :
                    return 'int'
                elif leftType == 'float' or rightType == 'float':
                    return 'float'
                elif leftType == 'float' and rightType == 'int':
                    return 'float'

            elif expression.LT() or expression.GT() or expression.LTEQ() or expression.GTEQ() or expression.EQQ() or expression.NOTEQ():
                return 'bool'
            elif expression.MOD():
                if leftType == 'int' and rightType == 'int':
                    return 'int'
        
        elif leftType == 'str' and rightType == 'str':
            if expression.APPEND():
                return 'str'
            elif expression.LT() or expression.GT() or expression.LTEQ() or expression.GTEQ() or expression.EQQ() or expression.NOTEQ():
                return 'bool'
            
        elif leftType == 'bool' and rightType == 'bool':
            if expression.AND() or expression.OR() or expression.XOR() or expression.NOT():
                return 'bool'
            elif expression.LT() or expression.GT() or expression.LTEQ() or expression.GTEQ() or expression.EQQ() or expression.NOTEQ():
                return 'bool'
        if leftType == rightType and expression.EQ():
            return leftType
        
        return None

        
    def getDataType(self,expression:PaulGrammarParser.ExpressionContext):
        if expression.STRING_LITRAL():
            return 'str'
        elif expression.INT_LITRAL():
            return 'int'
        elif expression.FLOAT_LITRAL():
            return 'float'
        elif expression.BOOL_LITRAL():
            return 'bool'
        elif expression.ID():
            if expression.ID().getText() in self.program:
                if self.program[expression.ID().getText()] == None:
                    return None
                else:
                    return self.program[expression.ID().getText()]["type"]
            else:
                return None
        elif expression.expression():
            if len(expression.expression()) == 2:
                left = self.getDataType(expression.expression(0))
                right = self.getDataType(expression.expression(1))
                if left == None or right == None:
                    return None
                else:
                    return self.getOperationType(expression,left,right)
            else:
                return self.getDataType(expression.expression(0))
        else:
            return None


class CodeGenerator:
    def __init__(self):
        self.code = []

    def loadExpression(self,expression:PaulGrammarParser.ExpressionContext):
        if expression.STRING_LITRAL():
            return 'str'
        elif expression.INT_LITRAL():
            return 'int'
        elif expression.FLOAT_LITRAL():
            return 'float'
        elif expression.BOOL_LITRAL():
            return 'bool'


class ProjectListner(ParseTreeListener):

    program = {

    }

    programStack = []

    errors = []

    labelCounter = 0

    symbol = {
        "str" : "S",
        "int" : "I",
        "float" : "F",
        "bool" : "B"
    }




    def enterProgram(self, ctx:PaulGrammarParser.ProgramContext):
        print("Program Started")

        pass

    # Exit a parse tree produced by PaulGrammarParser#program.
    def exitProgram(self, ctx:PaulGrammarParser.ProgramContext):
        print("Program Ended")
        pass


    def enterCondition(self, ctx:PaulGrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#condition.
    def exitCondition(self, ctx:PaulGrammarParser.ConditionContext):
        pass

    # Enter a parse tree produced by PaulGrammarParser#statement.
    def enterStatement(self, ctx:PaulGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#statement.
    def exitStatement(self, ctx:PaulGrammarParser.StatementContext):
        if ctx.parentCtx != None:
            if type(ctx.parentCtx) == PaulGrammarParser.IfStatementContext:
                self.programStack.append("jmp {}".format(self.labelCounter+1))
                self.programStack.append("label {}".format(self.labelCounter))
                self.labelCounter += 1

        

    # Enter a parse tree produced by PaulGrammarParser#block.
    def enterBlock(self, ctx:PaulGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#block.
    def exitBlock(self, ctx:PaulGrammarParser.BlockContext):
        if ctx.parentCtx != None:
            if type(ctx.parentCtx) == PaulGrammarParser.IfStatementContext:
                self.programStack.append("jmp {}".format(self.labelCounter+1))
                self.programStack.append("label {}".format(self.labelCounter))
                self.labelCounter += 1
        pass


        # Enter a parse tree produced by PaulGrammarParser#elseStatement.
    def enterElseStatement(self, ctx:PaulGrammarParser.ElseStatementContext):

        pass

    # Exit a parse tree produced by PaulGrammarParser#elseStatement.
    def exitElseStatement(self, ctx:PaulGrammarParser.ElseStatementContext):
        pass

    # Enter a parse tree produced by PaulGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:PaulGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:PaulGrammarParser.IfStatementContext):
        self.programStack.append("label {}".format(self.labelCounter))
        self.labelCounter += 1
        pass

    # Enter a parse tree produced by PaulGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:PaulGrammarParser.WhileStatementContext):
        self.programStack.append("label {}".format(self.labelCounter))
        self.labelCounter += 1
        pass

    # Exit a parse tree produced by PaulGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:PaulGrammarParser.WhileStatementContext):
        self.programStack.append("jmp {}".format(self.labelCounter-1))
        self.programStack.append("label {}".format(self.labelCounter))
        self.labelCounter += 1
        pass

    # Enter a parse tree produced by PaulGrammarParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:PaulGrammarParser.DoWhileStatementContext):
        self.programStack.append("label {}".format(self.labelCounter))
        self.labelCounter += 1
        pass

    # Exit a parse tree produced by PaulGrammarParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:PaulGrammarParser.DoWhileStatementContext):
        self.programStack.append("fjmp {}".format(self.labelCounter+1))
        self.programStack.append("jmp {}".format(self.labelCounter-1))
        self.labelCounter += 1
        self.programStack.append("label {}".format(self.labelCounter))
        self.labelCounter += 1
        pass
        

    # Enter a parse tree produced by PaulGrammarParser#writeStatement.
    def enterWriteStatement(self, ctx:PaulGrammarParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by PaulGrammarParser#writeStatement.
    def exitWriteStatement(self, ctx:PaulGrammarParser.WriteStatementContext):
        td = 1
        if type(ctx.expression()) == list:
            td = len(ctx.expression())
        self.programStack.append("print {}".format(td))
        pass

    # Enter a parse tree produced by PaulGrammarParser#readStatement.
    def enterReadStatement(self, ctx:PaulGrammarParser.ReadStatementContext):
        for x in ctx.ID():
            if x.getText() in self.program:
                self.programStack.append("read {}".format(self.symbol[self.program[x.getText()]["type"]]))
                self.programStack.append("save {}".format(x.getText()))
                
        pass

    # Exit a parse tree produced by PaulGrammarParser#readStatement.
    def exitReadStatement(self, ctx:PaulGrammarParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by PaulGrammarParser#expression.
    def enterExpression(self, ctx:PaulGrammarParser.ExpressionContext):
        pushed = False
        if ctx.STRING_LITRAL():
            self.programStack.append("push {} {}".format("S",ctx.STRING_LITRAL().getText()))
        elif ctx.INT_LITRAL():
            self.programStack.append("push {} {}".format("I",ctx.INT_LITRAL().getText()))
            pushed = True
        elif ctx.FLOAT_LITRAL():
            self.programStack.append("push {} {}".format("F",ctx.FLOAT_LITRAL().getText()))
        elif ctx.BOOL_LITRAL():
            self.programStack.append("push {} {}".format("B",ctx.BOOL_LITRAL().getText()))

        if pushed:
            if ctx.parentCtx != None:
                if type(ctx.parentCtx) == PaulGrammarParser.ExpressionContext:
                    if type(ctx.parentCtx.expression()) == list:
                        if len(ctx.parentCtx.expression()) == 2:
                            leftType = DataTypeResolver(self.program).getDataType(ctx.parentCtx.expression(0))
                            rightType = DataTypeResolver(self.program).getDataType(ctx.parentCtx.expression(1))
                            if not ctx.parentCtx.EQ() and not ctx.parentCtx.AND() and not ctx.parentCtx.OR() and not ctx.parentCtx.XOR() and not ctx.parentCtx.NOT():
                                if leftType == 'float' and rightType == 'int':
                                    self.programStack.append("itof")
                                elif leftType == 'int' and rightType == 'float':
                                    self.programStack.append("itof")
                            
                           
                        

        

        
        
        if ctx != None:
            try:
                dtype = DataTypeResolver(self.program)
                pt = dtype.getDataType(ctx)
                if pt == None and ctx.start.line != 1:
                    self.errors.append("[ERROR] -> INVALID EXPRESSION LINE:{}".format(ctx.start.line))
            except Exception as e:
                self.errors.append(e)
                self.errors.append("<---------COMPILER ERROR--------->Exp")
            
        

    # Exit a parse tree produced by PaulGrammarParser#expression.
    def exitExpression(self, ctx:PaulGrammarParser.ExpressionContext):
        if ctx.ID():
            if ctx.parentCtx != None:
                if type(ctx.parentCtx) == PaulGrammarParser.ExpressionContext:
                    if not ctx.parentCtx.EQ():
                        if ctx.ID().getText() in self.program:
                            self.programStack.append("load {}".format(ctx.ID().getText()))
                else:
                    if ctx.ID().getText() in self.program:
                        self.programStack.append("load {}".format(ctx.ID().getText()))
                        
        #datares = DataTypeResolver(self.program)
        #if len(ctx.expression()) == 2:
        #    leftType = datares.getDataType(ctx.expression(0))
        #    rightType = datares.getDataType(ctx.expression(1))
        #    if leftType == 'float' and rightType == 'int':
        #        self.programStack.append("itof")


        
        if ctx.ADD():
            self.programStack.append("add")
        elif ctx.SUB():
            if len(ctx.expression()) == 2:
                self.programStack.append("sub")
            else:
                self.programStack.append("uminus")
        elif ctx.MUL():
            self.programStack.append("mul")
        elif ctx.DIV():
            self.programStack.append("div")
        elif ctx.MOD():
            self.programStack.append("mod")
        elif ctx.LT():
            self.programStack.append("lt")
        elif ctx.GT():
            self.programStack.append("gt")
        elif ctx.LTEQ():
            self.programStack.append("lteq")
        elif ctx.GTEQ():
            self.programStack.append("gteq")
        elif ctx.EQQ():
            self.programStack.append("eq")
        elif ctx.NOTEQ():
            self.programStack.append("eq")
            self.programStack.append("not")
        elif ctx.AND():
            self.programStack.append("and")
        elif ctx.OR():
            self.programStack.append("or")
        elif ctx.XOR():
            self.programStack.append("xor")
        elif ctx.NOT():
            self.programStack.append("not")
        elif ctx.APPEND():
            self.programStack.append("concat")
        elif ctx.EQ():
            leftChild = ctx.expression(0)
            if leftChild.ID() != None:
                if leftChild.ID().getText() in self.program:
                    self.programStack.append("save {}".format(leftChild.ID().getText()))
                    self.programStack.append("load {}".format(leftChild.ID().getText()))

        if ctx.parentCtx != None:
            if type(ctx.parentCtx) == PaulGrammarParser.IfStatementContext:
                self.programStack.append("fjmp {}".format(self.labelCounter))
            elif type(ctx.parentCtx) == PaulGrammarParser.WhileStatementContext:
                self.programStack.append("fjmp {}".format(self.labelCounter))




    def enterAssignment(self, ctx:PaulGrammarParser.AssignmentContext):
        for x in ctx.ID():
            if x.getText() not in self.program:
                self.errors.append("[ERROR] -> Variable '{}' not declared LINE:{}".format(x.getText(),ctx.start.line))
                return
            else:
                try:
                    datares = DataTypeResolver(self.program)
                    if ctx.condition():
                        if datares.getDataType(ctx.condition().expression(0)) == 'bool':
                            leftType = datares.getDataType(ctx.condition().expression(1))
                            rightType = datares.getDataType(ctx.condition().expression(2))
                            if leftType == rightType :
                                if leftType != self.program[x.getText()]["type"]:
                                    self.errors.append("[ERROR] -> Assignment Type mismatch Expected {} but got {} LINE:{}".format(self.program[x.getText()]["type"],leftType,ctx.start.line))
                            else:
                                self.errors.append("[ERROR] -> Condition types mismatch LINE:{}".format(ctx.start.line))
                        else:
                            self.errors.append("[ERROR] -> Condition not boolean LINE:{}".format(ctx.start.line))
                    else:

                        if datares.getDataType(ctx.expression()) in ['float','int'] and  self.program[x.getText()]["type"] == 'float':
                            
                            pass
                        elif datares.getDataType(ctx.expression()) != self.program[x.getText()]["type"]:
                            self.errors.append("[ERROR] -> Assignment Type mismatch Expected {} but got {} LINE:{}".format(self.program[x.getText()]["type"],datares.getDataType(ctx.expression()),ctx.start.line))
                except Exception as e:
                    self.errors.append(e)
                    self.errors.append("<---------COMPILER ERROR--------->")
                    return
                
                

        pass

    def exitAssignment(self, ctx:PaulGrammarParser.AssignmentContext):
        datares = DataTypeResolver(self.program)
        for x in ctx.ID():
            if x.getText() in self.program:
                if datares.getDataType(ctx.expression()) == "int" and  self.program[x.getText()]["type"] == 'float':
                    self.programStack.append("itof")
                    pass
                self.programStack.append("save {}".format(x.getText()))
                self.programStack.append("load {}".format(x.getText()))
                self.programStack.append("pop")
          
                
                

    def enterDeclaration(self,ctx:PaulGrammarParser.DeclarationContext):
        dtype = None
        symbol = None
        data = {
            "S" :"\"\"",
            "I" : 0,
            "F" : 0.0,
            "B" : "false"
        }
        if ctx.STRING():
            symbol = 'S'
            dtype = 'str'
        elif ctx.FLOAT():
            symbol = 'F'
            dtype = 'float'
        elif ctx.INT():
            symbol = 'I'
            dtype = 'int'
        elif ctx.BOOL():
            symbol = 'B'
            dtype = 'bool'
        if dtype != None:
            for x in ctx.ID():
                if x.getText() in self.program:
                    self.errors.append("[ERROR] -> Variable already declared LINE:{}".format(ctx.start.line))
                else:
                    self.program[x.getText()] = {"value":None,"type":dtype}
                    self.programStack.append("push {} {}".format(symbol,data[symbol]))
                    self.programStack.append("save {}".format(x.getText()))
                    
        else:
            self.errors.append("[ERROR] -> Unkown datatype LINE:{}".format(ctx.start.line))






def main():

    file = open("input.txt","r")
    lines = file.read()

    stream = InputStream(lines)

    #input_stream = FileStream("input.txt")
    lexer = PaulGrammarLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = PaulGrammarParser(tokens)
    tree = parser.expression()
    #print(tree.toStringTree(recog=parser))


    

    listener = ProjectListner()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    if len(listener.errors) > 0:
        for x in listener.errors:
            print(x)
    else:
        result = open("output.txt","w")
        for x in listener.programStack:
            result.write(x)
            result.write("\n")
        result.close()
        print("Compilation Successful")

if __name__ == '__main__':
    main()
