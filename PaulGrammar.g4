
grammar PaulGrammar;

program: statement+ EOF;



statement: 
        ';'| declaration
        | assignment
        | ifStatement
        | condition
        | writeStatement
        | readStatement
        | block
        | whileStatement
        | doWhileStatement
        | forStatement
        | elseStatement
        | expression ';';

block: '{' statement* '}';
ifStatement: IF '(' expression ')' block (elseStatement)? | IF '(' expression ')' statement ';'? (elseStatement ';'?)?;
elseStatement: ELSE block | ELSE statement;
whileStatement: 'while' '(' expression ')' block;
doWhileStatement: 'do' block 'while' '(' expression ')' ';';
assignment: ID '=' (ID '=')*? expression ';' | ID '=' (ID '=')*? condition ;
writeStatement: WRITE expression (',' expression)*? ';'';'?;
readStatement: READ ID (',' ID)* ';';
declaration: (INT | FLOAT | BOOL | STRING) ID (',' ID)* ';';
condition : expression '?' expression ':' expression ';';
forStatement: 'for' '(' expression ';' expression ';' expression ')' block;

expression :
    INT_LITRAL | FLOAT_LITRAL | BOOL_LITRAL | STRING_LITRAL
    | ID
    | writeStatement statement*?
    | declaration statement*?
    | assignment statement*?
    | readStatement statement*?
    | ifStatement statement*?
    | elseStatement statement*?
    | whileStatement statement*?
    | doWhileStatement statement*?
    | forStatement statement*?
    | ';' statement*?
    |'(' expression ')'
    | expression postfix = ('++' | '--')
    | prefix = ('+' | '-' | '++' | '--' | '~' | '!') expression                                 
    | expression bop = ('*' | '/' | '%') expression           
    | expression bop = ('+' | '-') expression                 
    | expression ('<' '<' | '>' '>' '>' | '>' '>') expression 
    | expression bop = ('<=' | '>=' | '>' | '<') expression   
    | expression bop = ('==' | '!=') expression                     
    | expression bop = '&' expression                               
    | expression bop = '^' expression                               
    | expression bop = '|' expression                                
    | expression (AND | OR | XOR) expression    
    | expression bop = '.' expression                               
    | expression bop = '||' expression       
    | <assoc = right> expression bop = (
        '='
        |'+='
        | '-='
        | '*='
        | '/='
        | '&='
        | '|='
        | '^='
        | '>>='
        | '>>>='
        | '<<='
        | '%='
    ) expression;

// Tokens
EQ: '=' ;
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
APPEND: '.';
XOR: '^';
AND: '&&';
OR: '||';
GT: '>';
LT: '<';
EQQ: '==';
GTEQ: '>=';
LTEQ: '<=';
NOTEQ: '!=';
NOT: '!';
ITOF: 'itof';
PUSH: 'push';
POP: 'pop';
LOAD: 'load';
SAVE: 'save';
LABEL: 'label';
JMP: 'jmp';
FJMP: 'fjmp';
PRINT: 'print';
READ: 'read';
WRITE: 'write';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';

TYPES: (INT | FLOAT | BOOL | STRING);



INT_LITRAL: [0-9]+;

FLOAT_LITRAL: [0-9]+ '.' [0-9]* | '.' [0-9]+;

BOOL_LITRAL: 'true' | 'false';

STRING_LITRAL: '"' (~["\\] | EscapeSequence)* '"';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

NEWLINE: '\r'? '\n' -> skip;


WS           : [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT      : '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT : '//' ~[\r\n]*    -> channel(HIDDEN);


fragment EscapeSequence:
    '\\' 'u005c'? [btnfr"'\\]
    | '\\' 'u005c'? ([0-3]? [0-7])? [0-7]
;

