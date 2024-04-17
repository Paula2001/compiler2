// Generated from PaulGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PaulGrammarParser}.
 */
public interface PaulGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PaulGrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PaulGrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PaulGrammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PaulGrammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(PaulGrammarParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(PaulGrammarParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(PaulGrammarParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(PaulGrammarParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void enterElseStatement(PaulGrammarParser.ElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void exitElseStatement(PaulGrammarParser.ElseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(PaulGrammarParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(PaulGrammarParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileStatement(PaulGrammarParser.DoWhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileStatement(PaulGrammarParser.DoWhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(PaulGrammarParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(PaulGrammarParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteStatement(PaulGrammarParser.WriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteStatement(PaulGrammarParser.WriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(PaulGrammarParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(PaulGrammarParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(PaulGrammarParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(PaulGrammarParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(PaulGrammarParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(PaulGrammarParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(PaulGrammarParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(PaulGrammarParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PaulGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(PaulGrammarParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PaulGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(PaulGrammarParser.ExpressionContext ctx);
}