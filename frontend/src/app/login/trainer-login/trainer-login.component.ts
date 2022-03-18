import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

import { environment } from 'src/environments/environment';



@Component({
  selector: 'app-trainer-login',
  templateUrl: './trainer-login.component.html',
  styleUrls: ['./trainer-login.component.css']
})
export class TrainerLoginComponent implements OnInit {

  username: string = '';
  password: string = '';
  url: string = environment.API_URL + 'trainer/login';

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTrainerLogin() {
    this.router.navigate(['trainer-login'])
  }

  ngOnInit(): void {
  }

  loginTrainer() {

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
        localStorage.setItem('trainerId', response.user_id);
        this.router.navigate(['/trainer']);

      }else{
        alert('Login Failed' + response.message)
      }
    })
  }

}
