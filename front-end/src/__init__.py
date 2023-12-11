# from flask import Flask



# if __name__ == '__main__':
#     """
#     Must be placed at the end of the file.
#     """
    
#     # app.run(host = '192.168.1.46', port = 3000, debug = True)
#     # app.run(host = '127.0.0.1', port = 3000, debug = True)
#     app.run(host = '127.0.0.1', port = 9000, debug=True)
#     # app.run(host= "174.138.53.254" , port = 9000, debug = True)



# def ourPaths():
#     """
#     ourPaths() must be placed at the beginning of the file 
#     in order for the site to build and run.
    
#     ourPaths() must be called immediately after it ends.
    
#     Purpose: Initializes necessary variable for web app.
#     """
#     import os

#     global rootPath
#     rootPath = os.path.abspath(os.getcwd())
#     print(f"rootPath: {rootPath}")
    
#     # global webletIndex
#     # webletIndex =  "index.html"
    
#     global passwordTA
#     global passwordTC
#     pwFile = (rootPath + "\\Misc_Folder\\SQL\\TA_ourPySQL.txt")
#     with open(pwFile, 'r') as passFile:
#         passwordTA = passFile.readline()
#     pwFile = (rootPath + "\\Misc_Folder\\SQL\\TC_ourPySQL.txt")
#     with open(pwFile, 'r') as passFile:
#         passwordTC = passFile.readline()
#         # Password for the databases gets read from a file, so
#         # that it is not explicitly stored here in the code.
#         # MySQL Injections are scary.
# ourPaths()# Must be placed at beginning of file.



# # import mysql.connector

# # Connections to the MySQL Databases
# # catalog = mysql.connector.connect(
# #     host="174.138.53.254",
# #     user="TheAuditor",
# #     password=passwordTA,
# #     database="catalog"
# # )
# # reviews = mysql.connector.connect(
# #     host="174.138.53.254",
# #     user="TheAuditor",
# #     password=passwordTA,
# #     database="reviews"
# # )
# # progress = mysql.connector.connect(
# #     host="174.138.53.254",
# #     user="TheAuditor",
# #     password=passwordTA,
# #     database="progress"
# # )

# # myCatalog = catalog.cursor(prepared=True)
# # myReviews = reviews.cursor(prepared=True)
# # myProgress = progress.cursor(prepared=True)
