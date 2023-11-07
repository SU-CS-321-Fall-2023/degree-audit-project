% Course Title, CRN, Term Description
% Major Name, Major Abbreviation
% major(Degree, Major_Abbreviation, Major_Name)

% To receive the details regarding a specific major, epecially for ones that have similar abbreviations:
% getDetails("BA", "EDUC", X) :- major("BA", "EDUC", X), courseDescription(X,Y).

% findMajor(Degree, Abbreviation, Full_Name, Majors) :-
%     findall((Degree, Abbreviation, Full_Name), major(Degree,Abbreviation,Full_Name), Majors),
%     write_to_file('majors.csv', Majors).
findMajor(Degree, Abbreviation, Full_Name, Majors) :-
    findall((Degree, Abbreviation, Full_Name), major(Degree,Abbreviation,Full_Name), Majors),
    forall(Degree=Degree, write_to_file('majors.txt', Majors)).
    % write_to_file('majors.csv', Majors).
    % print(Majors).
    % forall(major(Degree, Abbreviation, Full_Name)=Majors, (print(major(Degree, Abbreviation, Full_Name)))).


% fileSave(Filename, List, Mode) :-
%     must_be(oneof([write, append]), Mode),
%     setup_call_cleanup(
%         open(FileName, Mode, File),
%         forall(
%             member(Element,List),
%             (
%                 write(File, Element),
%                 write(File, ' ')
%             )
%         ),
%         close(File)).

% portray(majors(Majors)) :- nl(Majors), maplist(writeln, Majors).

% Define a predicate to write data to a file
write_to_file(File, Data) :-
    open(File, write, Stream),  % Open the file for writing (creates/overwrites)
    writeq(Stream, Data),        % Write the data to the file
    close(Stream).              % Close the file

% Example usage
% write_to_file('pickles.txt', 'Hello, Prolog!\n').
% write_to_file('pickles.txt', 'This is a new line.\n').

% Read and display the contents of the file
read_file(File) :-
    open(File, read, Stream),
    repeat,
    read_line_to_string(Stream, Line),
    (   Line == end_of_file
    ->  true
    ;   writeln(Line),
        fail
    ),
    close(Stream).

% Example usage to read and display the contents of the file
% read_file('output.txt').


% write_list([]).
% write_to_file(Filename, Data) :-
%     open(Filename, append, Stream),
%     write(Stream, Data),
%     write(Stream, '\n'),
%     % write_to_file(Filename, Data),
%     close(Stream).
% write_list([H|T]) :-
%     open('pickles.txt', write, Stream),
%     write(Stream, H),
%     write(Stream, '\n'),
%     write_list(T),
%     close(Stream).

find_majorByDegree(Degree, Majors) :- 
    findMajor(Degree, Abbreviation, Full_Name, Majors).
    % forall(Degree=Degree, writef('%t', ([Degree, Abbreviation, Full_Name]))).
    % write_to_file('pickles.txt', Majors).
    % write_to_file('pickles.txt', Majors).
    % write_list([Majors|Majors]).


    % forall(Degree="BA", write_term((Degree, Abbreviation, Full_Name), [ portray(true), numbervars(true), quoted(true), no_lists(false) ])).
    % forall(Majors, (writef('\n'), writeln(Majors))).
    % forall(Majors, (writeln(("BA", "AMST", "American Studies"), Term))).
        % find_majorByDegree(Degree, Majors).




    % myWrite(Majors).
    % member(("BA", "ENGL", "English"), Majors),
    % writef('%t\n', Majors).
    % find_majorByDegree(Degree, Majors).
    % print(Degree), print(Abbreviation), print(Full_Name), write(Majors).
    % atom_concat(Degree, Abbreviation, L), atom_concat(L, Full_Name, L), print(L).
    % print_term(Degree, [ portray(true), numbervars(true), quoted(true)]).
% find_majorByAbbrev(Abbreviation, Majors) :- 
%     findMajor(Degree, Abbreviation, Full_Name, Majors).
%     % atom_concat(Degree, Abbreviation, Abbreviation), atom_concat(Abbreviation, Full_Name, Abbreviation).
%     % print_term((Abbreviation), [ portray(true), numbervars(true), quoted(true)]).
% find_majorByName(Full_Name, Majors) :- 
%     findMajor(Degree, Abbreviation, Full_Name, Majors).
%     % atom_concat(Abbreviation, Full_Name, Full_Name), atom_concat(Degree, Full_Name, Full_Name),
%     % print_term(Majors, [ portray(true), numbervars(true), quoted(true), no_lists(false)]).
% % find_majorByDegree2(Degree, Majors) :- findall(X, major(Degree,_,X), Majors). 


% getDetails("BA", "EDUC", X) :- courseDescription(X,Y).

courseDescription("Elementary Education", ": That is a child-friendly major.").

% TODO: Differentiate between "Elementary Education" and "General Studies in Education"
% TODO: Differentiate between "Economics" and "Global Development"
% TODO: Differentiate between "Environmental Studies" and "Environmental Science"
% Bachelor of Arts
major("BA", "AMST", "American Studies").
major("BA", "COMM", "Communication and Media Studies").
major("BA", "DIGA", "Digital Arts").
major("BA", "EDUC", "Elementary Education").
major("BA", "ENGL", "English").
major("BA", "ENSS", "Environmental Studies").
major("BA", "EDUC", "General Studies in Education").
major("BA", "ECON", "Global Development").
major("BA", "HIST", "History").
major("BA", "INSU", "International Studies").
major("BA", "ARTH", "Museum and Curatorial Studies").
major("BA", "PHIL", "Philosophy").
major("BA", "POLI", "Political Science").
major("BA", "MGMT", "Public Management").
major("BA", "RELS", "Religious Studies").
major("BA", "REES", "Russian, East European and Eurasian Studies").
major("BA", "SSCI", "Social Science").
major("BA", "SOCI", "Sociology").
major("BA", "ARTS", "Studio Art").
major("BA", "THEA", "Theatre Arts").
major("BA", "FREN", "World Languages and Cultures - French and Francophone Studies").
major("BA", "SPAN", "World Languages and Cultures - Hispanic Studies").
major("BA", "GERM", "World Languages and Cultures - German Studies").
major("BA", "WLGC", "World Languages and Cultures - Translator").

% Bachelor of Science
major("BS", "BIOL", "Aquatic and Marine Biology").
major("BS", "MATH/FINA", "Applied Mathematics - Actuarial and Financial Mathematics").
major("BS", "MATH/CSCI", "Applied Mathematics - Data Science").
major("BS", "MATH/PHYS", "Applied Mathematics - Physics").
major("BS", "MATH/STAT", "Applied Mathematics - Statistics").
major("BS", "BIOL/CHEM", "Biochemistry").
major("BS", "BIOL", "Biology").
major("BS", "CHEM", "Chemistry").
major("BS", "CINF", "Computer Information Systems").
major("BS", "CSCI", "Computer Science").
major("BS", "CSEC", "Cybersecurity").
major("BS", "DIGA", "Digital Arts").
major("BS", "ECON", "Economics").
major("BS", "ENSS", "Environmental Science").
major("BS", "HLSC", "Health Sciences").
major("BS", "MATH", "Mathematics").
major("BS", "BIOL", "Molecular and Cellular Biology").
major("BS", "PHYS", "Physics").
major("BS", "PHYS/CSCI", "Physics - Applied Physics").
major("BS", "PHYS/BIOL", "Physics - Biophysics").
major("BS", "PSYC", "Psychology").
major("BS", "PUBH", "Public Health").

% Bachelor of Business Administration
major("BBA", "ACCT", "Accounting").
major("BBA", "SOBA", "Business Administration").
major("BBA", "BSAN", "Business Systems and Analytics").
major("BBA", "ECON", "Economics").
major("BBA", "ENTP", "Entrepreneurship").
major("BBA", "FENT", "Family Enterprise Management").
major("BBA", "FINA", "Finance").
major("BBA", "CSCI", "Business Flex Major").
major("BBA", "HRMT", "Human Resource Management").
major("BBA", "INTL", "International Business").
major("BBA", "MGMT", "Management").
major("BBA", "MKTG", "Marketing").
major("BBA", "SALS", "Professional Sales").

% Bachelor of Music
major("BM", "MUSC", "BM in Composition").
major("BM", "MUSC", "BM in Performance (Guitar)").
major("BM", "MUSC", "BM in Theory").
major("BM", "MUSC", "BM in Performance (Orchestral Instrument)").
major("BM", "MUSC", "BM in Performance (Organ)").
major("BM", "MUSC", "BM in Performance (Piano)").
major("BM", "MUSC", "BM in Performance (Voice)").
major("BM", "MUSC", "BM with Elective Studies in a Specific Outside Field").
major("BM", "MUSC", "BM with Emphasis in Business").
% Bachelor of Music Education
major("BME", "MUSC", "BME (Instrumental/General)").
major("BME", "MUSC", "BME (Vocal/General)").
% Bachelor of Arts in Music
major("BA in Music", "MUSC", "BA in Music").

% :- (listing(major("BA", Y, Z))).

% Minors
minor("AFST", "Africana Studies").
minor("AMST", "American Studies").
minor("ANTH", "Anthropology").
minor("ARTH", "Art History").
minor("ASIA", "Asian Studies").
minor("BIOL", "Biology").
minor("CHEM", "Chemistry").
minor("COMM", "Communication and Media Studies").
minor("CSCI", "Computer Science").
minor("ENCW", "Creative Writing").
minor("DATA", "Data Analytics").
minor("DIGA", "Digital Arts").
minor("ECON", "Economics").
minor("EDUC", "Education").
minor("ENGL", "English").
minor("ENSS", "Environmental Studies").
minor("FREN", "French").
minor("GEND", "Gender Studies").
minor("GERM", "German").
minor("GLOB", "Global Development").
minor("HLSC", "Health Sciences").
minor("HIST", "History").
minor("INSU", "International Studies").
minor("JWST", "Jewish Studies").
minor("JOUR", "Journalism").
minor("LALS", "Latin American and Latino Studies").
minor("MATH", "Mathematics").
minor("PHIL", "Philosophy").
minor("PHYS", "Physics").
minor("POLI", "Political Science").
minor("PSYC", "Psychology").
minor("PUBH", "Public Health").
minor("RELS", "Religious Studies").
minor("RUSS", "Russian").
minor("REES", "Russian, East European, and Eurasian Studies").
minor("SOCI", "Sociology").
minor("SPAN", "Spanish").
% minor("Studio Art").
minor("FOOD", "Sustainable Food Systems").
minor("THEA", "Theatre Arts").
minor("WLGC", "World Language").

% Administered through the School of Business Administration.
minor("Accounting").
minor("Applied Statistics").
minor("Business Administration").
minor("Business Systems and Analytics").
minor("Business Law").
minor("Entrepreneurship").
minor("Family Enterprise").
minor("Finance").
minor("Human Resource Management").
minor("International Business").
minor("Management").
minor("Marketing").
minor("Professional Sales").
minor("Sport Business").

% Administered through the School of Music.
minor("General Minor in Music").
minor("Music Technology").
% Command to list all offered minors.
% :- listing(minor).


% Course Descriptions
cas("AMST").
cas("COMM").
cas("CSCI").
cas("DIGA").


% f(a).
% f(b).
% f(c).
% g(a).
% g(b).
% g(c).
% h(b).
% h(c).
% k(X) :- f(X), g(X), h(X).
