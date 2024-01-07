# edzyaml
A github action to pass values to a remote github repo yaml file ( Mostly useful for k8s yamls configs gitops )


----
How to use ?

```yaml
  uses: Aadeshkale/edzyaml@main
  with:
    git_username: Aadeshkale
    git_user_email: aadesh****595@gmail.com
    git_repo: Aadeshkale/kube-cd
    git_token: ${{ secrets.git_token }}
    yaml_file_path: deployment.yaml
    yaml_key_path: 'spec.template.spec.containers.0.image'    
    yaml_value: welcome-app:asdf-tg
```

Variable discription

 ``` * git_username :-    Username of github repo
  * git_email :-       Email of github repo
  * git_repo :-        Target github repo that contains yaml file
  * git_token :-       Github personal access token for target repo with write access
  * yaml_file_path:-   Path to yaml file 
  * yaml_key_path:-    A complete path to yaml sperated by '.' key needs to pass value
                       example,'spec.template.spec.containers.0.image'    
      
      * If you have list of object then you need to specify index no i.e 0,1,2...
      * Till 9 occurance it will support
      * If you passing same value for update it will show exception i.e Everything up to date

  * yaml_value:-            Value you want to pass  
 ```
Screenhots
![using_custom_action](https://github.com/Aadeshkale/edzyaml/assets/40000735/8e1f82ed-4aad-4956-b4b0-a16592789548)



