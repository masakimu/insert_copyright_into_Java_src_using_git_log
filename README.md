# insert_copyright_into_Java_src_using_git_log

Simple python scripts that I insert copyright into Java source codes comitted in [Mass++ ver4](https://github.com/masspp/mspp4) repository. 

1. Before use the scripts, default license headers should be inserted into source codes by [License Maven Plugin](http://code.mycila.com/license-maven-plugin/).

I used format of license like this:
 <start string of license header e.g. 'BSD 3-Clause License'>
  
 @author masakimu
 @since 2018
 
 <end string of license header  e.g. 'Copyright (c) 2018, Mass++ Users Group>
  
2. place extract_author_date_from_git_log.py at top folder of your git repository
3. run extract_author_date_from_git_log.py to create author information lists
   $ python extract_author_date_from_git_log.py > list_file_author_date.txt
4. run license_headers.py
   $ python license_headers.py list_file_author_date.txt 'BSD 3-Clause License' 'Copyright' > update_headers.log
  
  
