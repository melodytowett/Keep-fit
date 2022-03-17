import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';


import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-signup-trainee',
  templateUrl: './signup-trainee.component.html',
  styleUrls: ['./signup-trainee.component.css']
})
export class SignupTraineeComponent implements OnInit {

  constructor(private readonly http: HttpClient) {}

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

    this.http.post(this.url, body, httpOptions).subscribe(data=>{
      console.log(data);
    })
  }
}
