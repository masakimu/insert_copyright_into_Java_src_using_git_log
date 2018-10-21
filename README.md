# insert_copyright_into_Java_src_using_git_log


Simple python scripts to insert copyright into Java source codes.
I used them to update license headers of comitted source codes in [Mass++ ver4](https://github.com/masspp/mspp4) repository. 


1. Before using these scripts, initial license headers should be inserted into source codes. I used [License Maven Plugin](http://code.mycila.com/license-maven-plugin/) for Java program.

Following format/structure of license header is assumed:
> <start string of license header e.g. 'BSD 3-Clause License'>
>  
> (license statements)
>
> @author masakimu
> 
> @since 2018
>  
>  <end string of license header  e.g. 'Copyright (c) 2018, Mass++ Users Group>

2. place all python scripts at the top folder of your git repository, and change current directory to the folder.
3. create git log with file names:
>   $ git log --name-only > git_log_with_filenames.txt
4. run extract_author_date_from_git_log.py to generate file author information list
>   $ python extract_author_date_from_git_log.py git_log_with_filenames.txt > list_file_author_date.txt
5. run update_file_headers.py to update license header of source codes using file author information list
>   $ python update_file_header.py list_file_author_date.txt "BSD 3-Clause License" "Copyright (c) 2018, Mass++ Users Group" > update_headers.log
