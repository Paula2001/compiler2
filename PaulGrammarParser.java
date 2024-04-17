// Generated from PaulGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PaulGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, EQ=26, ADD=27, SUB=28, MUL=29, DIV=30, MOD=31, APPEND=32, XOR=33, 
		AND=34, OR=35, GT=36, LT=37, EQQ=38, GTEQ=39, LTEQ=40, NOTEQ=41, NOT=42, 
		ITOF=43, PUSH=44, POP=45, LOAD=46, SAVE=47, LABEL=48, JMP=49, FJMP=50, 
		PRINT=51, READ=52, WRITE=53, IF=54, ELSE=55, WHILE=56, DO=57, INT=58, 
		FLOAT=59, BOOL=60, STRING=61, TYPES=62, INT_LITRAL=63, FLOAT_LITRAL=64, 
		BOOL_LITRAL=65, STRING_LITRAL=66, ID=67, NEWLINE=68, WS=69, COMMENT=70, 
		LINE_COMMENT=71;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_block = 2, RULE_ifStatement = 3, 
		RULE_elseStatement = 4, RULE_whileStatement = 5, RULE_doWhileStatement = 6, 
		RULE_assignment = 7, RULE_writeStatement = 8, RULE_readStatement = 9, 
		RULE_declaration = 10, RULE_condition = 11, RULE_forStatement = 12, RULE_expression = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "block", "ifStatement", "elseStatement", "whileStatement", 
			"doWhileStatement", "assignment", "writeStatement", "readStatement", 
			"declaration", "condition", "forStatement", "expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "')'", "','", "'?'", "':'", "'for'", 
			"'++'", "'--'", "'~'", "'&'", "'|'", "'+='", "'-='", "'*='", "'/='", 
			"'&='", "'|='", "'^='", "'>>='", "'>>>='", "'<<='", "'%='", "'='", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'.'", "'^'", "'&&'", "'||'", "'>'", "'<'", 
			"'=='", "'>='", "'<='", "'!='", "'!'", "'itof'", "'push'", "'pop'", "'load'", 
			"'save'", "'label'", "'jmp'", "'fjmp'", "'print'", "'read'", "'write'", 
			"'if'", "'else'", "'while'", "'do'", "'int'", "'float'", "'bool'", "'string'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "EQ", "ADD", "SUB", "MUL", "DIV", "MOD", "APPEND", "XOR", 
			"AND", "OR", "GT", "LT", "EQQ", "GTEQ", "LTEQ", "NOTEQ", "NOT", "ITOF", 
			"PUSH", "POP", "LOAD", "SAVE", "LABEL", "JMP", "FJMP", "PRINT", "READ", 
			"WRITE", "IF", "ELSE", "WHILE", "DO", "INT", "FLOAT", "BOOL", "STRING", 
			"TYPES", "INT_LITRAL", "FLOAT_LITRAL", "BOOL_LITRAL", "STRING_LITRAL", 
			"ID", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PaulGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PaulGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PaulGrammarParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				statement();
				}
				}
				setState(31); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & -4616185219605586410L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 15L) != 0) );
			setState(33);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public WriteStatementContext writeStatement() {
			return getRuleContext(WriteStatementContext.class,0);
		}
		public ReadStatementContext readStatement() {
			return getRuleContext(ReadStatementContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public DoWhileStatementContext doWhileStatement() {
			return getRuleContext(DoWhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public ElseStatementContext elseStatement() {
			return getRuleContext(ElseStatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(50);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				declaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(37);
				assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(38);
				ifStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(39);
				condition();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(40);
				writeStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(41);
				readStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(42);
				block();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(43);
				whileStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(44);
				doWhileStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(45);
				forStatement();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(46);
				elseStatement();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(47);
				expression(0);
				setState(48);
				match(T__0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(T__1);
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -4616185219605586410L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 15L) != 0)) {
				{
				{
				setState(53);
				statement();
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(PaulGrammarParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ElseStatementContext elseStatement() {
			return getRuleContext(ElseStatementContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterIfStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitIfStatement(this);
		}
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ifStatement);
		try {
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				match(IF);
				setState(62);
				match(T__3);
				setState(63);
				expression(0);
				setState(64);
				match(T__4);
				setState(65);
				block();
				setState(67);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(66);
					elseStatement();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				match(IF);
				setState(70);
				match(T__3);
				setState(71);
				expression(0);
				setState(72);
				match(T__4);
				setState(73);
				statement();
				setState(75);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(74);
					match(T__0);
					}
					break;
				}
				setState(81);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
				case 1:
					{
					setState(77);
					elseStatement();
					setState(79);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						setState(78);
						match(T__0);
						}
						break;
					}
					}
					break;
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseStatementContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(PaulGrammarParser.ELSE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ElseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterElseStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitElseStatement(this);
		}
	}

	public final ElseStatementContext elseStatement() throws RecognitionException {
		ElseStatementContext _localctx = new ElseStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_elseStatement);
		try {
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(85);
				match(ELSE);
				setState(86);
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				match(ELSE);
				setState(88);
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(PaulGrammarParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterWhileStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitWhileStatement(this);
		}
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(WHILE);
			setState(92);
			match(T__3);
			setState(93);
			expression(0);
			setState(94);
			match(T__4);
			setState(95);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoWhileStatementContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(PaulGrammarParser.DO, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(PaulGrammarParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public DoWhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doWhileStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterDoWhileStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitDoWhileStatement(this);
		}
	}

	public final DoWhileStatementContext doWhileStatement() throws RecognitionException {
		DoWhileStatementContext _localctx = new DoWhileStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_doWhileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(DO);
			setState(98);
			block();
			setState(99);
			match(WHILE);
			setState(100);
			match(T__3);
			setState(101);
			expression(0);
			setState(102);
			match(T__4);
			setState(103);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(PaulGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PaulGrammarParser.ID, i);
		}
		public List<TerminalNode> EQ() { return getTokens(PaulGrammarParser.EQ); }
		public TerminalNode EQ(int i) {
			return getToken(PaulGrammarParser.EQ, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignment);
		try {
			int _alt;
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				match(ID);
				setState(106);
				match(EQ);
				setState(111);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(107);
						match(ID);
						setState(108);
						match(EQ);
						}
						} 
					}
					setState(113);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				}
				setState(114);
				expression(0);
				setState(115);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
				match(ID);
				setState(118);
				match(EQ);
				setState(123);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(119);
						match(ID);
						setState(120);
						match(EQ);
						}
						} 
					}
					setState(125);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
				}
				setState(126);
				condition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteStatementContext extends ParserRuleContext {
		public TerminalNode WRITE() { return getToken(PaulGrammarParser.WRITE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public WriteStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_writeStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterWriteStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitWriteStatement(this);
		}
	}

	public final WriteStatementContext writeStatement() throws RecognitionException {
		WriteStatementContext _localctx = new WriteStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_writeStatement);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(WRITE);
			setState(130);
			expression(0);
			setState(135);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(131);
					match(T__5);
					setState(132);
					expression(0);
					}
					} 
				}
				setState(137);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			setState(138);
			match(T__0);
			setState(140);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(139);
				match(T__0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadStatementContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(PaulGrammarParser.READ, 0); }
		public List<TerminalNode> ID() { return getTokens(PaulGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PaulGrammarParser.ID, i);
		}
		public ReadStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_readStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterReadStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitReadStatement(this);
		}
	}

	public final ReadStatementContext readStatement() throws RecognitionException {
		ReadStatementContext _localctx = new ReadStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_readStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			match(READ);
			setState(143);
			match(ID);
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(144);
				match(T__5);
				setState(145);
				match(ID);
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(151);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(PaulGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PaulGrammarParser.ID, i);
		}
		public TerminalNode INT() { return getToken(PaulGrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(PaulGrammarParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(PaulGrammarParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(PaulGrammarParser.STRING, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitDeclaration(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4323455642275676160L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(154);
			match(ID);
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(155);
				match(T__5);
				setState(156);
				match(ID);
				}
				}
				setState(161);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(162);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			expression(0);
			setState(165);
			match(T__6);
			setState(166);
			expression(0);
			setState(167);
			match(T__7);
			setState(168);
			expression(0);
			setState(169);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterForStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitForStatement(this);
		}
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_forStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(T__8);
			setState(172);
			match(T__3);
			setState(173);
			expression(0);
			setState(174);
			match(T__0);
			setState(175);
			expression(0);
			setState(176);
			match(T__0);
			setState(177);
			expression(0);
			setState(178);
			match(T__4);
			setState(179);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public Token prefix;
		public Token bop;
		public Token postfix;
		public TerminalNode INT_LITRAL() { return getToken(PaulGrammarParser.INT_LITRAL, 0); }
		public TerminalNode FLOAT_LITRAL() { return getToken(PaulGrammarParser.FLOAT_LITRAL, 0); }
		public TerminalNode BOOL_LITRAL() { return getToken(PaulGrammarParser.BOOL_LITRAL, 0); }
		public TerminalNode STRING_LITRAL() { return getToken(PaulGrammarParser.STRING_LITRAL, 0); }
		public TerminalNode ID() { return getToken(PaulGrammarParser.ID, 0); }
		public WriteStatementContext writeStatement() {
			return getRuleContext(WriteStatementContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ReadStatementContext readStatement() {
			return getRuleContext(ReadStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public ElseStatementContext elseStatement() {
			return getRuleContext(ElseStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public DoWhileStatementContext doWhileStatement() {
			return getRuleContext(DoWhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ADD() { return getToken(PaulGrammarParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(PaulGrammarParser.SUB, 0); }
		public TerminalNode NOT() { return getToken(PaulGrammarParser.NOT, 0); }
		public TerminalNode MUL() { return getToken(PaulGrammarParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(PaulGrammarParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(PaulGrammarParser.MOD, 0); }
		public List<TerminalNode> LT() { return getTokens(PaulGrammarParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(PaulGrammarParser.LT, i);
		}
		public List<TerminalNode> GT() { return getTokens(PaulGrammarParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(PaulGrammarParser.GT, i);
		}
		public TerminalNode LTEQ() { return getToken(PaulGrammarParser.LTEQ, 0); }
		public TerminalNode GTEQ() { return getToken(PaulGrammarParser.GTEQ, 0); }
		public TerminalNode EQQ() { return getToken(PaulGrammarParser.EQQ, 0); }
		public TerminalNode NOTEQ() { return getToken(PaulGrammarParser.NOTEQ, 0); }
		public TerminalNode XOR() { return getToken(PaulGrammarParser.XOR, 0); }
		public TerminalNode AND() { return getToken(PaulGrammarParser.AND, 0); }
		public TerminalNode OR() { return getToken(PaulGrammarParser.OR, 0); }
		public TerminalNode APPEND() { return getToken(PaulGrammarParser.APPEND, 0); }
		public TerminalNode EQ() { return getToken(PaulGrammarParser.EQ, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PaulGrammarListener ) ((PaulGrammarListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				{
				setState(182);
				match(INT_LITRAL);
				}
				break;
			case 2:
				{
				setState(183);
				match(FLOAT_LITRAL);
				}
				break;
			case 3:
				{
				setState(184);
				match(BOOL_LITRAL);
				}
				break;
			case 4:
				{
				setState(185);
				match(STRING_LITRAL);
				}
				break;
			case 5:
				{
				setState(186);
				match(ID);
				}
				break;
			case 6:
				{
				setState(187);
				writeStatement();
				setState(191);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(188);
						statement();
						}
						} 
					}
					setState(193);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
				}
				}
				break;
			case 7:
				{
				setState(194);
				declaration();
				setState(198);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(195);
						statement();
						}
						} 
					}
					setState(200);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
				}
				}
				break;
			case 8:
				{
				setState(201);
				assignment();
				setState(205);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(202);
						statement();
						}
						} 
					}
					setState(207);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
				}
				}
				break;
			case 9:
				{
				setState(208);
				readStatement();
				setState(212);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(209);
						statement();
						}
						} 
					}
					setState(214);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
				}
				}
				break;
			case 10:
				{
				setState(215);
				ifStatement();
				setState(219);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(216);
						statement();
						}
						} 
					}
					setState(221);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
				}
				}
				break;
			case 11:
				{
				setState(222);
				elseStatement();
				setState(226);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(223);
						statement();
						}
						} 
					}
					setState(228);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
				}
				}
				break;
			case 12:
				{
				setState(229);
				whileStatement();
				setState(233);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(230);
						statement();
						}
						} 
					}
					setState(235);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
				}
				}
				break;
			case 13:
				{
				setState(236);
				doWhileStatement();
				setState(240);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(237);
						statement();
						}
						} 
					}
					setState(242);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
				}
				}
				break;
			case 14:
				{
				setState(243);
				forStatement();
				setState(247);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(244);
						statement();
						}
						} 
					}
					setState(249);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
				}
				}
				break;
			case 15:
				{
				setState(250);
				match(T__0);
				setState(254);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(251);
						statement();
						}
						} 
					}
					setState(256);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
				}
				}
				break;
			case 16:
				{
				setState(257);
				match(T__3);
				setState(258);
				expression(0);
				setState(259);
				match(T__4);
				}
				break;
			case 17:
				{
				setState(261);
				((ExpressionContext)_localctx).prefix = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4398449171456L) != 0)) ) {
					((ExpressionContext)_localctx).prefix = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(262);
				expression(13);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(313);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(311);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(265);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(266);
						((ExpressionContext)_localctx).bop = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3758096384L) != 0)) ) {
							((ExpressionContext)_localctx).bop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(267);
						expression(13);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(268);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(269);
						((ExpressionContext)_localctx).bop = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((ExpressionContext)_localctx).bop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(270);
						expression(12);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(271);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(279);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
						case 1:
							{
							setState(272);
							match(LT);
							setState(273);
							match(LT);
							}
							break;
						case 2:
							{
							setState(274);
							match(GT);
							setState(275);
							match(GT);
							setState(276);
							match(GT);
							}
							break;
						case 3:
							{
							setState(277);
							match(GT);
							setState(278);
							match(GT);
							}
							break;
						}
						setState(281);
						expression(11);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(282);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(283);
						((ExpressionContext)_localctx).bop = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1855425871872L) != 0)) ) {
							((ExpressionContext)_localctx).bop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(284);
						expression(10);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(285);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(286);
						((ExpressionContext)_localctx).bop = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==EQQ || _la==NOTEQ) ) {
							((ExpressionContext)_localctx).bop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(287);
						expression(9);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(288);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(289);
						((ExpressionContext)_localctx).bop = match(T__12);
						setState(290);
						expression(8);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(291);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(292);
						((ExpressionContext)_localctx).bop = match(XOR);
						setState(293);
						expression(7);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(294);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(295);
						((ExpressionContext)_localctx).bop = match(T__13);
						setState(296);
						expression(6);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(297);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(298);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 60129542144L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(299);
						expression(5);
						}
						break;
					case 10:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(300);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(301);
						((ExpressionContext)_localctx).bop = match(APPEND);
						setState(302);
						expression(4);
						}
						break;
					case 11:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(303);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(304);
						((ExpressionContext)_localctx).bop = match(OR);
						setState(305);
						expression(3);
						}
						break;
					case 12:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(306);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(307);
						((ExpressionContext)_localctx).bop = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 134184960L) != 0)) ) {
							((ExpressionContext)_localctx).bop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(308);
						expression(1);
						}
						break;
					case 13:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(309);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(310);
						((ExpressionContext)_localctx).postfix = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
							((ExpressionContext)_localctx).postfix = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						break;
					}
					} 
				}
				setState(315);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 12);
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		case 3:
			return precpred(_ctx, 9);
		case 4:
			return precpred(_ctx, 8);
		case 5:
			return precpred(_ctx, 7);
		case 6:
			return precpred(_ctx, 6);
		case 7:
			return precpred(_ctx, 5);
		case 8:
			return precpred(_ctx, 4);
		case 9:
			return precpred(_ctx, 3);
		case 10:
			return precpred(_ctx, 2);
		case 11:
			return precpred(_ctx, 1);
		case 12:
			return precpred(_ctx, 14);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001G\u013d\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0004\u0000\u001e\b\u0000\u000b"+
		"\u0000\f\u0000\u001f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u00013\b\u0001\u0001\u0002\u0001\u0002\u0005\u00027\b\u0002"+
		"\n\u0002\f\u0002:\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003D\b\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003L\b\u0003\u0001\u0003\u0001\u0003\u0003\u0003P\b\u0003\u0003"+
		"\u0003R\b\u0003\u0003\u0003T\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004Z\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007n\b\u0007\n\u0007\f\u0007"+
		"q\t\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0005\u0007z\b\u0007\n\u0007\f\u0007}\t\u0007"+
		"\u0001\u0007\u0003\u0007\u0080\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0005\b\u0086\b\b\n\b\f\b\u0089\t\b\u0001\b\u0001\b\u0003\b\u008d\b\b"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0005\t\u0093\b\t\n\t\f\t\u0096\t\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u009e\b\n\n\n\f\n\u00a1"+
		"\t\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00be\b\r\n\r\f\r\u00c1\t\r"+
		"\u0001\r\u0001\r\u0005\r\u00c5\b\r\n\r\f\r\u00c8\t\r\u0001\r\u0001\r\u0005"+
		"\r\u00cc\b\r\n\r\f\r\u00cf\t\r\u0001\r\u0001\r\u0005\r\u00d3\b\r\n\r\f"+
		"\r\u00d6\t\r\u0001\r\u0001\r\u0005\r\u00da\b\r\n\r\f\r\u00dd\t\r\u0001"+
		"\r\u0001\r\u0005\r\u00e1\b\r\n\r\f\r\u00e4\t\r\u0001\r\u0001\r\u0005\r"+
		"\u00e8\b\r\n\r\f\r\u00eb\t\r\u0001\r\u0001\r\u0005\r\u00ef\b\r\n\r\f\r"+
		"\u00f2\t\r\u0001\r\u0001\r\u0005\r\u00f6\b\r\n\r\f\r\u00f9\t\r\u0001\r"+
		"\u0001\r\u0005\r\u00fd\b\r\n\r\f\r\u0100\t\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u0108\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u0118\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u0138\b\r\n\r\f\r\u013b"+
		"\t\r\u0001\r\ro{\u0087\u00bf\u00c6\u00cd\u00d4\u00db\u00e2\u00e9\u00f0"+
		"\u00f7\u00fe\u0001\u001a\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u0000\t\u0001\u0000:=\u0003\u0000\n\f\u001b"+
		"\u001c**\u0001\u0000\u001d\u001f\u0001\u0000\u001b\u001c\u0002\u0000$"+
		"%\'(\u0002\u0000&&))\u0001\u0000!#\u0001\u0000\u000f\u001a\u0001\u0000"+
		"\n\u000b\u0172\u0000\u001d\u0001\u0000\u0000\u0000\u00022\u0001\u0000"+
		"\u0000\u0000\u00044\u0001\u0000\u0000\u0000\u0006S\u0001\u0000\u0000\u0000"+
		"\bY\u0001\u0000\u0000\u0000\n[\u0001\u0000\u0000\u0000\fa\u0001\u0000"+
		"\u0000\u0000\u000e\u007f\u0001\u0000\u0000\u0000\u0010\u0081\u0001\u0000"+
		"\u0000\u0000\u0012\u008e\u0001\u0000\u0000\u0000\u0014\u0099\u0001\u0000"+
		"\u0000\u0000\u0016\u00a4\u0001\u0000\u0000\u0000\u0018\u00ab\u0001\u0000"+
		"\u0000\u0000\u001a\u0107\u0001\u0000\u0000\u0000\u001c\u001e\u0003\u0002"+
		"\u0001\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000"+
		"\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000"+
		"\u0000 !\u0001\u0000\u0000\u0000!\"\u0005\u0000\u0000\u0001\"\u0001\u0001"+
		"\u0000\u0000\u0000#3\u0005\u0001\u0000\u0000$3\u0003\u0014\n\u0000%3\u0003"+
		"\u000e\u0007\u0000&3\u0003\u0006\u0003\u0000\'3\u0003\u0016\u000b\u0000"+
		"(3\u0003\u0010\b\u0000)3\u0003\u0012\t\u0000*3\u0003\u0004\u0002\u0000"+
		"+3\u0003\n\u0005\u0000,3\u0003\f\u0006\u0000-3\u0003\u0018\f\u0000.3\u0003"+
		"\b\u0004\u0000/0\u0003\u001a\r\u000001\u0005\u0001\u0000\u000013\u0001"+
		"\u0000\u0000\u00002#\u0001\u0000\u0000\u00002$\u0001\u0000\u0000\u0000"+
		"2%\u0001\u0000\u0000\u00002&\u0001\u0000\u0000\u00002\'\u0001\u0000\u0000"+
		"\u00002(\u0001\u0000\u0000\u00002)\u0001\u0000\u0000\u00002*\u0001\u0000"+
		"\u0000\u00002+\u0001\u0000\u0000\u00002,\u0001\u0000\u0000\u00002-\u0001"+
		"\u0000\u0000\u00002.\u0001\u0000\u0000\u00002/\u0001\u0000\u0000\u0000"+
		"3\u0003\u0001\u0000\u0000\u000048\u0005\u0002\u0000\u000057\u0003\u0002"+
		"\u0001\u000065\u0001\u0000\u0000\u00007:\u0001\u0000\u0000\u000086\u0001"+
		"\u0000\u0000\u000089\u0001\u0000\u0000\u00009;\u0001\u0000\u0000\u0000"+
		":8\u0001\u0000\u0000\u0000;<\u0005\u0003\u0000\u0000<\u0005\u0001\u0000"+
		"\u0000\u0000=>\u00056\u0000\u0000>?\u0005\u0004\u0000\u0000?@\u0003\u001a"+
		"\r\u0000@A\u0005\u0005\u0000\u0000AC\u0003\u0004\u0002\u0000BD\u0003\b"+
		"\u0004\u0000CB\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000DT\u0001"+
		"\u0000\u0000\u0000EF\u00056\u0000\u0000FG\u0005\u0004\u0000\u0000GH\u0003"+
		"\u001a\r\u0000HI\u0005\u0005\u0000\u0000IK\u0003\u0002\u0001\u0000JL\u0005"+
		"\u0001\u0000\u0000KJ\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000"+
		"LQ\u0001\u0000\u0000\u0000MO\u0003\b\u0004\u0000NP\u0005\u0001\u0000\u0000"+
		"ON\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PR\u0001\u0000\u0000"+
		"\u0000QM\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RT\u0001\u0000"+
		"\u0000\u0000S=\u0001\u0000\u0000\u0000SE\u0001\u0000\u0000\u0000T\u0007"+
		"\u0001\u0000\u0000\u0000UV\u00057\u0000\u0000VZ\u0003\u0004\u0002\u0000"+
		"WX\u00057\u0000\u0000XZ\u0003\u0002\u0001\u0000YU\u0001\u0000\u0000\u0000"+
		"YW\u0001\u0000\u0000\u0000Z\t\u0001\u0000\u0000\u0000[\\\u00058\u0000"+
		"\u0000\\]\u0005\u0004\u0000\u0000]^\u0003\u001a\r\u0000^_\u0005\u0005"+
		"\u0000\u0000_`\u0003\u0004\u0002\u0000`\u000b\u0001\u0000\u0000\u0000"+
		"ab\u00059\u0000\u0000bc\u0003\u0004\u0002\u0000cd\u00058\u0000\u0000d"+
		"e\u0005\u0004\u0000\u0000ef\u0003\u001a\r\u0000fg\u0005\u0005\u0000\u0000"+
		"gh\u0005\u0001\u0000\u0000h\r\u0001\u0000\u0000\u0000ij\u0005C\u0000\u0000"+
		"jo\u0005\u001a\u0000\u0000kl\u0005C\u0000\u0000ln\u0005\u001a\u0000\u0000"+
		"mk\u0001\u0000\u0000\u0000nq\u0001\u0000\u0000\u0000op\u0001\u0000\u0000"+
		"\u0000om\u0001\u0000\u0000\u0000pr\u0001\u0000\u0000\u0000qo\u0001\u0000"+
		"\u0000\u0000rs\u0003\u001a\r\u0000st\u0005\u0001\u0000\u0000t\u0080\u0001"+
		"\u0000\u0000\u0000uv\u0005C\u0000\u0000v{\u0005\u001a\u0000\u0000wx\u0005"+
		"C\u0000\u0000xz\u0005\u001a\u0000\u0000yw\u0001\u0000\u0000\u0000z}\u0001"+
		"\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000"+
		"|~\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000~\u0080\u0003\u0016"+
		"\u000b\u0000\u007fi\u0001\u0000\u0000\u0000\u007fu\u0001\u0000\u0000\u0000"+
		"\u0080\u000f\u0001\u0000\u0000\u0000\u0081\u0082\u00055\u0000\u0000\u0082"+
		"\u0087\u0003\u001a\r\u0000\u0083\u0084\u0005\u0006\u0000\u0000\u0084\u0086"+
		"\u0003\u001a\r\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u0089\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0087\u0085\u0001"+
		"\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000\u0000\u0089\u0087\u0001"+
		"\u0000\u0000\u0000\u008a\u008c\u0005\u0001\u0000\u0000\u008b\u008d\u0005"+
		"\u0001\u0000\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008c\u008d\u0001"+
		"\u0000\u0000\u0000\u008d\u0011\u0001\u0000\u0000\u0000\u008e\u008f\u0005"+
		"4\u0000\u0000\u008f\u0094\u0005C\u0000\u0000\u0090\u0091\u0005\u0006\u0000"+
		"\u0000\u0091\u0093\u0005C\u0000\u0000\u0092\u0090\u0001\u0000\u0000\u0000"+
		"\u0093\u0096\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000"+
		"\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u0097\u0001\u0000\u0000\u0000"+
		"\u0096\u0094\u0001\u0000\u0000\u0000\u0097\u0098\u0005\u0001\u0000\u0000"+
		"\u0098\u0013\u0001\u0000\u0000\u0000\u0099\u009a\u0007\u0000\u0000\u0000"+
		"\u009a\u009f\u0005C\u0000\u0000\u009b\u009c\u0005\u0006\u0000\u0000\u009c"+
		"\u009e\u0005C\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009e\u00a1"+
		"\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000\u0000\u009f\u00a0"+
		"\u0001\u0000\u0000\u0000\u00a0\u00a2\u0001\u0000\u0000\u0000\u00a1\u009f"+
		"\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005\u0001\u0000\u0000\u00a3\u0015"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a5\u0003\u001a\r\u0000\u00a5\u00a6\u0005"+
		"\u0007\u0000\u0000\u00a6\u00a7\u0003\u001a\r\u0000\u00a7\u00a8\u0005\b"+
		"\u0000\u0000\u00a8\u00a9\u0003\u001a\r\u0000\u00a9\u00aa\u0005\u0001\u0000"+
		"\u0000\u00aa\u0017\u0001\u0000\u0000\u0000\u00ab\u00ac\u0005\t\u0000\u0000"+
		"\u00ac\u00ad\u0005\u0004\u0000\u0000\u00ad\u00ae\u0003\u001a\r\u0000\u00ae"+
		"\u00af\u0005\u0001\u0000\u0000\u00af\u00b0\u0003\u001a\r\u0000\u00b0\u00b1"+
		"\u0005\u0001\u0000\u0000\u00b1\u00b2\u0003\u001a\r\u0000\u00b2\u00b3\u0005"+
		"\u0005\u0000\u0000\u00b3\u00b4\u0003\u0004\u0002\u0000\u00b4\u0019\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b6\u0006\r\uffff\uffff\u0000\u00b6\u0108\u0005"+
		"?\u0000\u0000\u00b7\u0108\u0005@\u0000\u0000\u00b8\u0108\u0005A\u0000"+
		"\u0000\u00b9\u0108\u0005B\u0000\u0000\u00ba\u0108\u0005C\u0000\u0000\u00bb"+
		"\u00bf\u0003\u0010\b\u0000\u00bc\u00be\u0003\u0002\u0001\u0000\u00bd\u00bc"+
		"\u0001\u0000\u0000\u0000\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf\u00c0"+
		"\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00c0\u0108"+
		"\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2\u00c6"+
		"\u0003\u0014\n\u0000\u00c3\u00c5\u0003\u0002\u0001\u0000\u00c4\u00c3\u0001"+
		"\u0000\u0000\u0000\u00c5\u00c8\u0001\u0000\u0000\u0000\u00c6\u00c7\u0001"+
		"\u0000\u0000\u0000\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c7\u0108\u0001"+
		"\u0000\u0000\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9\u00cd\u0003"+
		"\u000e\u0007\u0000\u00ca\u00cc\u0003\u0002\u0001\u0000\u00cb\u00ca\u0001"+
		"\u0000\u0000\u0000\u00cc\u00cf\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001"+
		"\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000\u00ce\u0108\u0001"+
		"\u0000\u0000\u0000\u00cf\u00cd\u0001\u0000\u0000\u0000\u00d0\u00d4\u0003"+
		"\u0012\t\u0000\u00d1\u00d3\u0003\u0002\u0001\u0000\u00d2\u00d1\u0001\u0000"+
		"\u0000\u0000\u00d3\u00d6\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000"+
		"\u0000\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d5\u0108\u0001\u0000"+
		"\u0000\u0000\u00d6\u00d4\u0001\u0000\u0000\u0000\u00d7\u00db\u0003\u0006"+
		"\u0003\u0000\u00d8\u00da\u0003\u0002\u0001\u0000\u00d9\u00d8\u0001\u0000"+
		"\u0000\u0000\u00da\u00dd\u0001\u0000\u0000\u0000\u00db\u00dc\u0001\u0000"+
		"\u0000\u0000\u00db\u00d9\u0001\u0000\u0000\u0000\u00dc\u0108\u0001\u0000"+
		"\u0000\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00de\u00e2\u0003\b\u0004"+
		"\u0000\u00df\u00e1\u0003\u0002\u0001\u0000\u00e0\u00df\u0001\u0000\u0000"+
		"\u0000\u00e1\u00e4\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e3\u0108\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e5\u00e9\u0003\n\u0005\u0000"+
		"\u00e6\u00e8\u0003\u0002\u0001\u0000\u00e7\u00e6\u0001\u0000\u0000\u0000"+
		"\u00e8\u00eb\u0001\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000\u0000\u0000"+
		"\u00e9\u00e7\u0001\u0000\u0000\u0000\u00ea\u0108\u0001\u0000\u0000\u0000"+
		"\u00eb\u00e9\u0001\u0000\u0000\u0000\u00ec\u00f0\u0003\f\u0006\u0000\u00ed"+
		"\u00ef\u0003\u0002\u0001\u0000\u00ee\u00ed\u0001\u0000\u0000\u0000\u00ef"+
		"\u00f2\u0001\u0000\u0000\u0000\u00f0\u00f1\u0001\u0000\u0000\u0000\u00f0"+
		"\u00ee\u0001\u0000\u0000\u0000\u00f1\u0108\u0001\u0000\u0000\u0000\u00f2"+
		"\u00f0\u0001\u0000\u0000\u0000\u00f3\u00f7\u0003\u0018\f\u0000\u00f4\u00f6"+
		"\u0003\u0002\u0001\u0000\u00f5\u00f4\u0001\u0000\u0000\u0000\u00f6\u00f9"+
		"\u0001\u0000\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f7\u00f5"+
		"\u0001\u0000\u0000\u0000\u00f8\u0108\u0001\u0000\u0000\u0000\u00f9\u00f7"+
		"\u0001\u0000\u0000\u0000\u00fa\u00fe\u0005\u0001\u0000\u0000\u00fb\u00fd"+
		"\u0003\u0002\u0001\u0000\u00fc\u00fb\u0001\u0000\u0000\u0000\u00fd\u0100"+
		"\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000\u0000\u00fe\u00fc"+
		"\u0001\u0000\u0000\u0000\u00ff\u0108\u0001\u0000\u0000\u0000\u0100\u00fe"+
		"\u0001\u0000\u0000\u0000\u0101\u0102\u0005\u0004\u0000\u0000\u0102\u0103"+
		"\u0003\u001a\r\u0000\u0103\u0104\u0005\u0005\u0000\u0000\u0104\u0108\u0001"+
		"\u0000\u0000\u0000\u0105\u0106\u0007\u0001\u0000\u0000\u0106\u0108\u0003"+
		"\u001a\r\r\u0107\u00b5\u0001\u0000\u0000\u0000\u0107\u00b7\u0001\u0000"+
		"\u0000\u0000\u0107\u00b8\u0001\u0000\u0000\u0000\u0107\u00b9\u0001\u0000"+
		"\u0000\u0000\u0107\u00ba\u0001\u0000\u0000\u0000\u0107\u00bb\u0001\u0000"+
		"\u0000\u0000\u0107\u00c2\u0001\u0000\u0000\u0000\u0107\u00c9\u0001\u0000"+
		"\u0000\u0000\u0107\u00d0\u0001\u0000\u0000\u0000\u0107\u00d7\u0001\u0000"+
		"\u0000\u0000\u0107\u00de\u0001\u0000\u0000\u0000\u0107\u00e5\u0001\u0000"+
		"\u0000\u0000\u0107\u00ec\u0001\u0000\u0000\u0000\u0107\u00f3\u0001\u0000"+
		"\u0000\u0000\u0107\u00fa\u0001\u0000\u0000\u0000\u0107\u0101\u0001\u0000"+
		"\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0108\u0139\u0001\u0000"+
		"\u0000\u0000\u0109\u010a\n\f\u0000\u0000\u010a\u010b\u0007\u0002\u0000"+
		"\u0000\u010b\u0138\u0003\u001a\r\r\u010c\u010d\n\u000b\u0000\u0000\u010d"+
		"\u010e\u0007\u0003\u0000\u0000\u010e\u0138\u0003\u001a\r\f\u010f\u0117"+
		"\n\n\u0000\u0000\u0110\u0111\u0005%\u0000\u0000\u0111\u0118\u0005%\u0000"+
		"\u0000\u0112\u0113\u0005$\u0000\u0000\u0113\u0114\u0005$\u0000\u0000\u0114"+
		"\u0118\u0005$\u0000\u0000\u0115\u0116\u0005$\u0000\u0000\u0116\u0118\u0005"+
		"$\u0000\u0000\u0117\u0110\u0001\u0000\u0000\u0000\u0117\u0112\u0001\u0000"+
		"\u0000\u0000\u0117\u0115\u0001\u0000\u0000\u0000\u0118\u0119\u0001\u0000"+
		"\u0000\u0000\u0119\u0138\u0003\u001a\r\u000b\u011a\u011b\n\t\u0000\u0000"+
		"\u011b\u011c\u0007\u0004\u0000\u0000\u011c\u0138\u0003\u001a\r\n\u011d"+
		"\u011e\n\b\u0000\u0000\u011e\u011f\u0007\u0005\u0000\u0000\u011f\u0138"+
		"\u0003\u001a\r\t\u0120\u0121\n\u0007\u0000\u0000\u0121\u0122\u0005\r\u0000"+
		"\u0000\u0122\u0138\u0003\u001a\r\b\u0123\u0124\n\u0006\u0000\u0000\u0124"+
		"\u0125\u0005!\u0000\u0000\u0125\u0138\u0003\u001a\r\u0007\u0126\u0127"+
		"\n\u0005\u0000\u0000\u0127\u0128\u0005\u000e\u0000\u0000\u0128\u0138\u0003"+
		"\u001a\r\u0006\u0129\u012a\n\u0004\u0000\u0000\u012a\u012b\u0007\u0006"+
		"\u0000\u0000\u012b\u0138\u0003\u001a\r\u0005\u012c\u012d\n\u0003\u0000"+
		"\u0000\u012d\u012e\u0005 \u0000\u0000\u012e\u0138\u0003\u001a\r\u0004"+
		"\u012f\u0130\n\u0002\u0000\u0000\u0130\u0131\u0005#\u0000\u0000\u0131"+
		"\u0138\u0003\u001a\r\u0003\u0132\u0133\n\u0001\u0000\u0000\u0133\u0134"+
		"\u0007\u0007\u0000\u0000\u0134\u0138\u0003\u001a\r\u0001\u0135\u0136\n"+
		"\u000e\u0000\u0000\u0136\u0138\u0007\b\u0000\u0000\u0137\u0109\u0001\u0000"+
		"\u0000\u0000\u0137\u010c\u0001\u0000\u0000\u0000\u0137\u010f\u0001\u0000"+
		"\u0000\u0000\u0137\u011a\u0001\u0000\u0000\u0000\u0137\u011d\u0001\u0000"+
		"\u0000\u0000\u0137\u0120\u0001\u0000\u0000\u0000\u0137\u0123\u0001\u0000"+
		"\u0000\u0000\u0137\u0126\u0001\u0000\u0000\u0000\u0137\u0129\u0001\u0000"+
		"\u0000\u0000\u0137\u012c\u0001\u0000\u0000\u0000\u0137\u012f\u0001\u0000"+
		"\u0000\u0000\u0137\u0132\u0001\u0000\u0000\u0000\u0137\u0135\u0001\u0000"+
		"\u0000\u0000\u0138\u013b\u0001\u0000\u0000\u0000\u0139\u0137\u0001\u0000"+
		"\u0000\u0000\u0139\u013a\u0001\u0000\u0000\u0000\u013a\u001b\u0001\u0000"+
		"\u0000\u0000\u013b\u0139\u0001\u0000\u0000\u0000\u001e\u001f28CKOQSYo"+
		"{\u007f\u0087\u008c\u0094\u009f\u00bf\u00c6\u00cd\u00d4\u00db\u00e2\u00e9"+
		"\u00f0\u00f7\u00fe\u0107\u0117\u0137\u0139";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}