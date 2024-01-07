# edzyaml
A github action to pass values to a remote github repo yaml file ( Mostly useful for k8s yamls configs gitops )


----
How to use ?






* git_username :- Username of github repo

* git_email :- Email of github repo

* git_repo :- Target github repo that contains yaml file

* git_token: Github personal access token for target repo with write access

* yaml_file_path: Path to yaml file 

* yaml_key_path: A complete path to yaml sperated by '.' key needs to pass value
  example,'spec.template.spec.containers.0.image'    
    Note:- *  If you have list of object then you need to specify index no i.e 0,1,2...
           *  Till 9 occurance it will support
           *  If you passing same value for update it will show exception i.e Everything up to date

yaml_value: Value you want to pass  
