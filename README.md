# Chaabhi-Assignment

Approach
1.Implement vector embeddings on the given dataset and store them in a Vector DB
like Qdrant.Implement an LLM on the DB that can give contextual answers to the queries
strictly from the database.
2.Deploying this model using flask (API)


Instructions to run the code.

For the LLM part(Chaabhi_LLM.ipynb)
1. put the path of the CSV file in the CSV_path variable to run the code
2. the code is run on google colab
3. Therefore, some files that are generated for showing ouptuts like Output1.pkl,bertmodel.pkl, qs_client.pkl,stmodel.pkl
4. So the pathing of these files are  such that when the code is run, these files will be generated to /content/(files) path and will be used from there
5. So when running the code in google colab only CSV_path is required 

OUTPUTS for the Queries
1.After running the Chaabhi_LLM.ipynb file it will going to give a result.txt file

Installation
1.Install required dependencies
2.Go in API Folder
3.Type flask run 

Result

QUERY INPUT: suggest me one product for bathing
OUTPUT: Deodorant Soap 
PREDICTION SCORE 0.0006341218249872327

Referred Product: Lime Soap 100 gm Buy 4 Get 1 Free + Deodorant Soap- Cool 100 gm Buy 4 Get 1 Free



QUERY INPUT: what is price of chia seeds
OUTPUT: 145.25 
PREDICTION SCORE 0.5620284080505371

Referred Product: Chia Seeds



QUERY INPUT: what is most loved hair product
OUTPUT: thick, curly or frizzy hair 
PREDICTION SCORE 0.13841083645820618

Referred Product: Hair Vital Bioactive Oil With Olive, Castor, Almond, Jojoba, Rosemary, Tea Tree



QUERY INPUT: suggest one  Anti- Bacterial Scrub Pad
OUTPUT: Scotch brite 
PREDICTION SCORE 0.11101531237363815

Referred Product: Scrub Pad - Anti- Bacterial, Regular



QUERY INPUT: price of Soan Papdi Special
OUTPUT: 65.0 
PREDICTION SCORE 0.6374332904815674

Referred Product: Soan Papdi



QUERY INPUT: what is most loved beauty product
OUTPUT: Brightening Beauty Pack 
PREDICTION SCORE 0.11473003774881363

Referred Product: Brightening Beauty Pack
