import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';


import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-login-trainee',
  templateUrl: './login-trainee.component.html',
  styleUrls: ['./login-trainee.component.css']
})
export class LoginTraineeComponent implements OnInit {

  
  username: string = '';
  password: string = '';
  url: string = environment.API_URL + 'trainee/login';

  constructor(private readonly http: HttpClient, private router: Router) {}

  ngOnInit(): void {
  }

  loginTrainee() {

    const body = {
      username: this.username,
      password: this.password
    }

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}

    this.http.post(this.url, body, httpOptions).subscribe(data=>{
      response = data
      if (response.status == 'success') {
        alert('Login Successful')
      }else{
        alert('Login Failed')
      }
    })
  }

}
