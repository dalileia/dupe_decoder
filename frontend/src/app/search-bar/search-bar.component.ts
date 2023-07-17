import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})

export class SearchBarComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  isHome(): boolean {
    const check = this.router.url;
    console.log(check)
    if (check == '/') {
      return false
    } return true
  }

  onSubmit(form: NgForm) {
    this.router.navigate(['product-search', form.value.search]);
  }

}
