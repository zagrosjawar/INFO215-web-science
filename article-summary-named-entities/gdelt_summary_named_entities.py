import csvfrom newspaper import Articlefrom urllib.parse import urlparseimport spacyfrom spacy.lang.en.stop_words import STOP_WORDSfrom string import punctuationfrom collections import Counterfrom heapq import nlargest'''I managed to get access to links provided in source file and write them to destination csv file.I could not access som links and get the following Error Messages:"451 Client Error: Unavailable For Legal Reasons" "403 Client Error: Forbidden", which means that the server understands the request, but is refusing to fulfill it.-Most of the comments are for me just to understand and practice the code.'''# Opening the CSV file -returns a file object# Creating a CSV reader object# Each row returned by the reader is a list of String elements containing the data found by removing the delimiters.with open("20230310091500.export.CSV", newline='\n') as csv_file:    csv_reader = csv.reader(csv_file, delimiter="\t", )    urls = set()  # to avoid repeated links    for row in csv_reader:        # Extract the URL from the last column of the row        url = row[-1]        # print(url)        # Parse the URL using urlparse        parsed_url = urlparse(url)        # Check if the parsed URL has a valid scheme and netloc        if parsed_url.scheme and parsed_url.netloc:            urls.add(url)# Summary and Entity names the extracted URLs using newspaper and spacy# 1.Initialization of spaCy text summarizationnlp = spacy.load("en_core_web_md")with open("named_entities.csv", mode="w", encoding="utf-8", newline='') as csv_file2:    csv_writer = csv.writer(csv_file2)    for url in urls:        try:            article = Article(url)            article.download()            article.parse()            # the article.summary is returning an empty summary. So I used spaCy to summarize article.text            # 2. Filtering tokens            doc = nlp(article.text)            keyword = []            stopwords = list(STOP_WORDS)            pos_tag = ["PROPN", "ADJ", "NOUN", "VERB"]  # PROPN proper noun            for token in doc:                if token.text in stopwords or token.text in punctuation:                    continue                if token.pos_ in pos_tag:                    keyword.append(token.text)            # 3. Normalization            freq_word = Counter(keyword)  # dictionary            freq_word.most_common(5)  # list of tuples            max_freq = Counter(keyword).most_common(5)[0][1]            for word in freq_word.keys():  # list of keys of dictionary                # print(freq_word[word])                freq_word[word] = (freq_word[word] / max_freq)  # Normalization; updating the dictionary            freq_word.most_common(5)            # 4.Weighting sentences            sent_strength = {}            for sent in doc.sents:                for word in sent:                    if word.text in freq_word.keys():  # the updated dictionary of words after normalization                        if sent in sent_strength.keys():                            sent_strength[sent] += freq_word[word.text]  # dictionary of words as keys and their                            # frequency as values; value + value                        else:                            sent_strength[sent] = freq_word[word.text]  # adds sent to the sen_strenght dict and                            # assign the value of                            # freq_word[word.text] to the sent.            # 5. Summarization sentences            summarized_sentences = nlargest(3, sent_strength, key=sent_strength.get)  # return list of largest 3 sent            final_sentences = [w.text for w in summarized_sentences]            summary = ' '.join(final_sentences)            # print(summary)            doc = nlp(summary)            named_entities = set([ent.text for ent in doc.ents if ent.label_ != ''])            csv_writer.writerow([url, ','.join(named_entities).replace('\n', ' ')])        except Exception as e:            print(f"Error {url}: {str(e)}")