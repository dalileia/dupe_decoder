import { HttpClientTestingModule } from '@angular/common/http/testing';
import { DebugElement } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { By } from '@angular/platform-browser';
import { RouterTestingModule } from '@angular/router/testing';

import { HttpService } from '../services/http.service';
import { HomeComponent } from './home.component';

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;//var que permite criar uma instancia do componente
  let de: DebugElement;
  let el: HTMLElement

  beforeEach(async () => {
    await TestBed.configureTestingModule({ //Testbed permite criar um modulo para o componente que está sendo testado
      imports: [HttpClientTestingModule, RouterTestingModule, FormsModule],
      providers: [HttpService],
      declarations: [HomeComponent] // como esse modulo está isolada, ele não consegue usar os serviços e componestes declarados em app.module.ts, então precisamos declarar tudo aqui
    })
      .compileComponents().then(() => {
        fixture = TestBed.createComponent(HomeComponent); //cria uma instância do HomeComponent (cria um ambiente)
        component = fixture.componentInstance; //ComponenteFixture permite interagir com o componente criado

        de = fixture.debugElement.query(By.css('form'));
        el = de.nativeElement
      });

  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('should call the onSubmit method', async(() => {
    spyOn(component, 'onSubmit');
    el = fixture.debugElement.query(By.css('button')).nativeElement;
    el.click();
    expect(component.onSubmit).toBeTruthy()
  }))

  it('should be rendered', () => {
    fixture.detectChanges()
    expect(fixture.nativeElement.querySelector('p')).toBeTruthy();
  });

});
