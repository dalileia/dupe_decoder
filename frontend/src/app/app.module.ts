import { LayoutModule } from '@angular/cdk/layout';
import { HttpClientModule } from '@angular/common/http';
import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { ProductSearchComponent } from './product-search/product-search.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { HttpService } from './services/http.service';
import { MaterialModule } from './shared/material.module';
import { ProductDisplayComponent } from './product-display/product-display.component';


@NgModule({
  declarations: [
    AppComponent,
    SearchBarComponent,
    HomeComponent,
    ProductDetailComponent,
    NavbarComponent,
    ProductDetailComponent,
    ProductSearchComponent,
    ProductSearchComponent,
    ProductDisplayComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    LayoutModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule
  ],
  exports: [FormsModule],
  providers: [HttpService],
  bootstrap: [AppComponent],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA
  ]
})
export class AppModule { }

