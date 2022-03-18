import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayGigComponent } from './display-gig.component';

describe('DisplayGigComponent', () => {
  let component: DisplayGigComponent;
  let fixture: ComponentFixture<DisplayGigComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DisplayGigComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplayGigComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
