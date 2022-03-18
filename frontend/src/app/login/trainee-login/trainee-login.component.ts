import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-trainee-login',
  templateUrl: './trainee-login.component.html',
  styleUrls: ['./trainee-login.component.css']
})
export class TraineeLoginComponent implements OnInit {

  constructor(private router: Router, private readonly http: HttpClient) { }
  gotoTraineeLogin() {
    this.router.navigate(['trainee-login'])
  }

  ngOnInit(): void {
  }

}
