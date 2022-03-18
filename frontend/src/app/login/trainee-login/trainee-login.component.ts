import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';


import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-trainee-login',
  templateUrl: './trainee-login.component.html',
  styleUrls: ['./trainee-login.component.css']
})
export class TraineeLoginComponent implements OnInit {

  username: string = '';
  password: string = '';
  url: string = environment.API_URL + 'trainee/login';

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTraineeLogin() {
    this.router.navigate(['trainee-login'])
  }

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
        this.router.navigate(['/trainee']);
        
      }else{
        alert('Login Failed')
      }
    })


  }

}
