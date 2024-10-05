def main(): 
    with open("./books/frankenstien.txt") as f:
        file_content = f.read()
   # to find the number of words in  the given book
    def word_count(file_text):
        words = file_text.split()
        return len(words) 
    word_count_result=word_count(file_content)
        
   #to find the number of characters in the given book      
        
    def char_count(file_text):
        dict={}
        words=  file_text.split()
        joined_words="".join(words)
        for char in joined_words:
          lower_case=  char.lower()
          if lower_case in dict:
              dict[lower_case]+=1
          else:
              dict[lower_case]=1
        return dict
    char_count_dict= char_count(file_content) 
    
#  to organise the data 
    def report(dictionary):
         
        report_list=[]
        for key in dictionary:
            sample_dict={"letter":key,"count":dictionary[key]}
            report_list.append(sample_dict)
       
        def sort_dict(dict):
            return dict["count"]
        report_list.sort(reverse=True,key=sort_dict)
        return report_list
    sorted_list= report(char_count_dict)  
    
    
    #printing the data
    
    def loggger(list,word_count):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for dict in list:
            print(f"the character '{dict['letter']}' was found {dict['count']} times" )
            
        print("--- End report ---")    
          
    loggger(sorted_list,word_count_result)      
        
            
main()
