import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  search: String = "";

  constructor(public router: Router) { }

  ngOnInit(): void {

  }


  onSubmit(form: NgForm) {
    this.router.navigate(['product-search', form.value.search]);
  }



}
