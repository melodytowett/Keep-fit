import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';


import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-signup-trainee',
  templateUrl: './signup-trainee.component.html',
  styleUrls: ['./signup-trainee.component.css']
})
export class SignupTraineeComponent implements OnInit {

  constructor(private readonly http: HttpClient, private router: Router) {}

  email :string = ''
  username: string = '';
  password: string = '';

  url: string = environment.API_URL + 'trainee/signup';

  ngOnInit(): void {
  }

  signupTrainee() {
    const body = {
      email: this.email,
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
        this.router.navigate(['/login-trainer']);
      }else{
        alert(response.message)
      }
    })
  }
}
