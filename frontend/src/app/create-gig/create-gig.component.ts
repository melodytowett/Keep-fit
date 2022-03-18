import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

import { environment } from 'src/environments/environment';


@Component({
  selector: 'app-create-gig',
  templateUrl: './create-gig.component.html',
  styleUrls: ['./create-gig.component.css']
})
export class CreateGigComponent implements OnInit {

  title :string = ''
  price: string = '';
  duration: string = '';
  category:string=''

  url: string = environment.API_URL + 'create_gig';

  constructor(private readonly http: HttpClient, private router: Router) {}

  ngOnInit(): void {
  }

  createGig() {
    const body = {
      title: this.title,
      price: this.price,
      duration: this.duration,
      category:this.category,

      trainerId : localStorage.getItem('trainerId')

    }
    

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })};

    let response:any={}

    this.http.post(this.url, body, httpOptions).subscribe(data=>{
      response = data
      if (response.status == 'success') {
        alert(response.message)
      }else{
        alert(response.message)
      }  
    })
  }

}
